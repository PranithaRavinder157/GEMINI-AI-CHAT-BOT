import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #e0f2fe, #f8fafc);
    }

    /* Main title */
    h1 {
        color: #111827 !important;
        text-align: center;
        font-size: 42px !important;
        font-weight: 700 !important;
    }

    /* All headings */
    h2, h3 {
        color: #111827 !important;
    }

    /* Normal text */
    p, label {
        color: #1f2937 !important;
    }

    /* Text area */
    textarea {
        background-color: white !important;
        color: #111827 !important;
        border: 2px solid #6366f1 !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        padding: 12px !important;
    }

    /* Text area when selected */
    textarea:focus {
        border: 2px solid #4f46e5 !important;
        box-shadow: 0 0 8px rgba(79, 70, 229, 0.3) !important;
    }

    /* Generate button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 17px;
        font-weight: 600;
        cursor: pointer;
        transition: 0.3s;
    }

    /* Button hover */
    .stButton > button:hover {
        background: linear-gradient(90deg, #4338ca, #6d28d9);
        transform: scale(1.02);
    }

    /* Response text */
    .response-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #6366f1;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.08);
        color: #111827;
        font-size: 16px;
        line-height: 1.6;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- App UI ----------------

st.title("🤖 Gemini AI Chatbot")

st.write("Ask Gemini Anything!")

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain artificial intelligence in simple words..."
)

if st.button("Generate Response"):

    if prompt:

        with st.spinner("Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("Response generated!")

        st.markdown(
            f"""
            <div class="response-box">
                {response.text}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a prompt.")
