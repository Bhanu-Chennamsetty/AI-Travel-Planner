### AI Travel Itinerary Planner
An AI-powered Travel Assistant built using **Streamlit** and **Google Gemini API**.

This application generates personalized travel itineraries, budget estimates, hotel recommendations, interactive maps, and includes a smart chatbot mode.

Designed as a long-term internship-level AI project demonstrating:
- Prompt Engineering
- State Management
- Interactive UI Design
- Multi-mode AI Assistant Architecture

---

# Features

## 🗺 Itinerary Mode
- Day-wise travel plan generation
- Travel style customization (Adventure, Luxury, Family, Solo, Romantic)
- Budget-level personalization
- AI-powered recommendations

## Budget Estimator
- Estimated daily travel cost
- Total trip cost
- Budget category handling (Budget / Mid-range / Luxury)

## Hotel Recommendations
- 3 AI-recommended hotels
- Price range breakdown
- Nearby attractions
- Justified recommendations

## Interactive Map View
- Destination overview using Streamlit map component

## Trip History
- Save generated trips
- View previous trips
- Clear trip history

## Travel Chatbot Mode
- Ask travel-related questions
- Packing suggestions
- Visa information
- Best time to visit
- Local travel advice

---

# Tech Stack

- **Frontend/UI:** Streamlit
- **Backend:** Python
- **AI Model:** Google Gemini 2.5 Flash
- **State Management:** Streamlit Session State
- **Data Handling:** Pandas
- **PDF Generation (Optional):** ReportLab
- **Deployment:** Streamlit Cloud Ready

---

# Project Structure

AI-Travel-Planner/
│
├── travel.py # Landing Page
├── pages/
│ └── planner.py # Main Planner Page
├── requirements.txt
└── README.md



---

# Complete Setup Guide (Step-by-Step From Scratch)

(1️) Install Python

Download and install Python from:

https://www.python.org/downloads/

During installation:
✔ Check "Add Python to PATH"

Verify installation:

```bash
python --version

(2️) Clone Repository

git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner

(3) Create Virtual Environment
python -m venv venv


Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

(4️) Install Dependencies
pip install streamlit google-genai pandas reportlab


OR if using requirements file:

pip install -r requirements.txt

(5️) Create requirements.txt (Optional)
pip freeze > requirements.txt

(6️) Get Google Gemini API Key

Visit: https://aistudio.google.com/app/apikey

Create new API key

Copy the key

(7️) Set Environment Variable
Windows (PowerShell):
setx GEMINI_API_KEY "your_api_key_here"


Restart VS Code after running this.

Mac/Linux:
export GEMINI_API_KEY="your_api_key_here"

(8️) Run the Application
streamlit run travel.py