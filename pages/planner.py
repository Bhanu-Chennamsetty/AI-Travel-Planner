import streamlit as st
from google import genai
import os
import pandas as pd

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈",
    layout="centered"
)

# ---------------- STYLING ---------------- #

st.markdown("""
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #87CEEB, #4facfe);
}

.app-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #f0f8ff;
    margin-bottom: 30px;
}

.section-title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: #1c1c1c;
    margin-bottom: 20px;
}

.itinerary-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.15);
}

.stButton>button {
    background-color: #ff6a00;
    color: white;
    font-size: 16px;
    padding: 10px 24px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD API ---------------- #

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found.")
    st.stop()

client = genai.Client(api_key=api_key)

# ---------------- SESSION STATE ---------------- #

if "trip_history" not in st.session_state:
    st.session_state.trip_history = []

# ---------------- HEADER ---------------- #

st.markdown('<div class="app-title">🌍 AI Travel Itinerary Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Plan smarter trips with AI-powered custom itineraries ✈</div>', unsafe_allow_html=True)

mode = st.radio("Select Mode:", ["🗺 Itinerary Mode", "🤖 Travel Chatbot"])

# =====================================================
# =============== ITINERARY MODE ======================
# =====================================================

if mode == "🗺 Itinerary Mode":

    st.markdown('<div class="section-title">✈ Plan Your Trip</div>', unsafe_allow_html=True)

    destination = st.text_input("🌍 Destination")
    days = st.number_input("📅 Days", min_value=1, step=1)
    nights = st.number_input("🌙 Nights", min_value=0, step=1)

    travel_style = st.selectbox(
        "🎯 Travel Style",
        ["Adventure", "Luxury", "Family", "Solo", "Romantic"]
    )

    budget_level = st.selectbox(
        "💰 Budget Level",
        ["Budget", "Mid-range", "Luxury"]
    )

    # -------- BUTTONS ALIGNED OPPOSITE -------- #

    col1, col2 = st.columns(2)

    with col1:
        generate = st.button("🚀 Generate Itinerary", use_container_width=True)

    with col2:
        back_home = st.button("⬅ Back to Home", use_container_width=True)

    # -------- NAVIGATION -------- #

    if back_home:
        st.switch_page("travel.py")

    # -------- FUNCTIONS -------- #

    def generate_itinerary():
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Create a detailed travel itinerary for {destination}
            for {days} days and {nights} nights.

            Travel Style: {travel_style}
            Budget Level: {budget_level}

            Format clearly as Day 1, Day 2 etc.
            Include attractions, food, travel tips.
            """
        )
        return response.text

    def generate_hotels():
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Suggest 3 hotels in {destination}
            for a {budget_level} traveler.
            Include:
            - Price range
            - Nearby attractions
            - Why recommended
            """
        )
        return response.text

    def estimate_budget():
        if budget_level == "Budget":
            daily = 2000
        elif budget_level == "Mid-range":
            daily = 5000
        else:
            daily = 12000
        total = daily * days
        return daily, total

    # -------- GENERATE ACTION -------- #

    if generate:
        if destination:

            with st.spinner("✨ AI is crafting your perfect trip..."):
                itinerary = generate_itinerary()
                hotels = generate_hotels()

            st.success("✅ Your itinerary is ready!")

            # Save history
            st.session_state.trip_history.append({
                "destination": destination,
                "days": days,
                "budget": budget_level
            })

            # Destination image
            st.image(
                f"https://source.unsplash.com/800x400/?{destination},travel",
                caption=destination,
                use_column_width=True
            )

            # Itinerary display
            sections = itinerary.split("Day")
            for section in sections:
                if section.strip():
                    st.markdown(
                        f'<div class="itinerary-card"><b>Day {section}</b></div>',
                        unsafe_allow_html=True
                    )

            # Budget Estimation
            daily_cost, total_cost = estimate_budget()
            st.subheader("💰 Budget Estimation")
            st.write(f"Estimated Daily Cost: ₹{daily_cost}")
            st.write(f"Estimated Total Trip Cost: ₹{total_cost}")

            # Hotels
            st.subheader("🏨 Recommended Hotels")
            st.markdown(hotels)

            # Map (placeholder coordinates)
            st.subheader("🗺 Location Overview")
            map_data = pd.DataFrame({
                "lat": [20.5937],
                "lon": [78.9629]
            })
            st.map(map_data)

        else:
            st.warning("Please enter a destination.")

    # -------- HISTORY -------- #

    if st.session_state.trip_history:
        st.subheader("📂 Saved Trips")

        for i, trip in enumerate(st.session_state.trip_history):
            st.write(
                f"{i+1}. {trip['destination']} - {trip['days']} Days - {trip['budget']}"
            )

        if st.button("🗑 Clear History"):
            st.session_state.trip_history = []
            st.success("History cleared!")

# =====================================================
# =============== CHATBOT MODE ========================
# =====================================================

if mode == "🤖 Travel Chatbot":

    st.markdown('<div class="section-title">🤖 Ask Travel Assistant</div>', unsafe_allow_html=True)

    user_question = st.text_input("Ask anything about travel:")

    if user_question:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_question
            )
        st.markdown("### 🤖 AI Response")
        st.write(response.text)
