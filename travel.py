import streamlit as st

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------
# BACKGROUND IMAGE + OVERLAY
# ---------------------------

page_bg = """
<style>

/* Full page background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1501785888041-af3ef285b470");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Stronger Dark Overlay */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.65);
    z-index: -1;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.75) !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 500;
}

/* Hero Section */
.hero {
    text-align: center;
    margin-top: 120px;
}

/* Title Styling */
.hero-title {
    font-size: 75px;
    font-weight: 900;
    color: #ffffff;
    text-shadow: 3px 3px 15px rgba(0,0,0,0.9);
}

/* Subtitle Styling */
.hero-subtitle {
    font-size: 26px;
    color: #f1f1f1;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    margin-bottom: 40px;
}

/* Floating airplane */
.airplane {
    font-size: 70px;
    color: #ffffff;
    text-shadow: 2px 2px 10px black;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-25px); }
    100% { transform: translateY(0px); }
}

/* Feature cards */
.feature-card {
    background: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.3);
    text-align: center;
    transition: 0.3s;
}

.feature-card:hover {
    transform: scale(1.05);
}

/* CTA Button */
.stButton>button {
    background-color: #ff6a00;
    color: white;
    font-size: 22px;
    padding: 12px 35px;
    border-radius: 12px;
    border: none;
}

.stButton>button:hover {
    background-color: #ff8c42;
}

</style>
"""


st.markdown(page_bg, unsafe_allow_html=True)

# ---------------------------
# HERO CONTENT
# ---------------------------

st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="airplane">✈</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">AI Travel Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Plan Smart. Travel Better. Explore More with Gemini AI</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# ---------------------------
# FEATURES SECTION
# ---------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Instant Itineraries</h3>
        <p>Generate detailed day-wise travel plans in seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🍽 Food & Attractions</h3>
        <p>Discover local cuisines and must-visit attractions.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>💡 Smart Travel Tips</h3>
        <p>Get budget suggestions and insider recommendations.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# ---------------------------
# CALL TO ACTION
# ---------------------------

center1, center2, center3 = st.columns([1,2,1])

with center2:
    if st.button("🚀 Start Planning Your Trip"):
        st.switch_page("pages/planner.py")
