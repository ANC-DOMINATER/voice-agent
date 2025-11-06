import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Customer Enquiry",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for minimalist clean styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container styling - Clean white background */
    .main {
        background: #f8f9fa;
        padding: 2rem 1rem;
        min-height: 100vh;
    }
    
    
    /* Header section - Above the card */
    .header {
        text-align: center;
        padding: 1.5rem 0 1.5rem 0;
        max-width: 900px;
        margin: 0 auto;
    }
    
    .header .small-title {
        color: #6366f1;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }
    
    .header h1 {
        font-size: 2.8rem;
        font-weight: 800;
        color: #1a1a1a;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .header .description {
        font-size: 1.05rem;
        color: #4a5568;
        line-height: 1.7;
        max-width: 700px;
        margin: 0 auto;
        padding-bottom: 1rem;
    }
    
    /* Section headers */
    h3 {
        color: #1a1a1a;
        font-weight: 700;
        font-size: 1.3rem;
        margin-bottom: 1.2rem;
        margin-top: 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Form styling - Clean minimal inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 1.5px solid #e2e8f0;
        padding: 12px 16px;
        font-size: 0.95rem;
        transition: all 0.2s ease;
        background: #ffffff;
        font-weight: 400;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        outline: none;
    }
    
    /* Labels */
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: #1a1a1a;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    /* Submit button - Purple gradient */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        padding: 14px 40px;
        font-size: 1rem;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        width: auto;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(99, 102, 241, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Checkbox styling */
    .stCheckbox {
        padding: 8px 0;
    }
    
    .stCheckbox label {
        font-weight: 400;
        color: #4a5568;
        font-size: 0.9rem;
    }
    
    /* Error messages - Red text */
    .stAlert {
        border-radius: 8px;
        padding: 12px 16px;
        font-weight: 500;
        font-size: 0.9rem;
        border: none;
    }
    
    div[data-baseweb="notification"] > div {
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    
    /* Success message */
    .success-message {
        background: #10b981;
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 20px 0;
    }
    
    /* Mobile optimization */
    @media (max-width: 768px) {
        .main {
            padding: 1rem 0.5rem;
        }
        
        .form-container {
            padding: 2rem 1.5rem;
            border-radius: 15px;
        }
        
        .header {
            padding: 1rem 0 1rem 0;
        }
        
        .header h1 {
            font-size: 2rem;
        }
        
        .header .description {
            font-size: 0.95rem;
        }
        
        h3 {
            font-size: 1.1rem;
        }
        
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            padding: 11px 14px;
            font-size: 0.9rem;
        }
        
        .stButton > button {
            padding: 12px 30px;
            font-size: 0.95rem;
            width: 100%;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
    <div class="header">
        <div class="small-title">✨ Get In Touch</div>
        <h1>We'd love to hear from you.<br>Let's start a conversation.</h1>
        <p class="description">
            🚀 Why Contact Us? Whether you have a question about our services, need assistance, or just 
            want to share feedback, our team is ready to help. Fill out the form below and we'll get back to 
            you within 24 hours.
        </p>
    </div>
""", unsafe_allow_html=True)

# Main content container
st.markdown('<div class="form-container">', unsafe_allow_html=True)

# Custom form matching n8n fields
with st.form("n8n_form", clear_on_submit=False):
    name = st.text_input("Name *", placeholder="")
    
    email = st.text_input("Email *", placeholder="")
    
    phone = st.text_input("Phone Number", placeholder="Include +91")
    
    subject = st.text_input("Subject", placeholder="")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Get a Call")
    
    if submitted:
        if not name or not email:
            st.error("❌ Please fill all required fields (Name and Email)")
        elif "@" not in email:
            st.error("❌ Please enter a valid email address")
        else:
            with st.spinner("Submitting..."):
                try:
                    response = requests.post(
                        "https://dominateranc.app.n8n.cloud/webhook/form",
                        json={
                            "name": name,
                            "email": email,
                            "phoneNumber": phone,
                            "subject": subject
                        },
                        headers={
                            "Content-Type": "application/json",
                            "Accept": "application/json"
                        },
                        timeout=15
                    )
                    
                    if response.status_code in [200, 201, 204]:
                        st.success("✅ Thank you! Your enquiry has been submitted successfully!")
                        st.balloons()
                    else:
                        st.error(f"❌ Submission failed. Status: {response.status_code}. Response: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Connection error: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

# No footer needed for cleaner look
