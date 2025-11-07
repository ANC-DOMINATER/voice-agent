# 🚀 AI Agent Call Automation – For Any Business

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://voice-agent-quantum-leap.streamlit.app)

> **🤖 AI Agent Demo**: The agent is trained on Quantum Leap Learning Solutions Pvt Ltd knowledge base. Feel free to ask any questions about Quantum Leap Learning Solutions Pvt Ltd in the deployment!

## Overview
This system automates customer calls and SMS follow-ups using **Streamlit**, **n8n**, and **Retell API**.  
It allows businesses to capture leads, trigger AI voice calls, and send follow-up SMS messages automatically — all without manual intervention.

---

## 🎬 Demo
Listen to a sample AI agent call:

[🎧 Play Demo Audio](https://gabalpha.github.io/read-audio/?p=https://github.com/ANC-DOMINATER/voice-agent/raw/main/.streamlit/demo.mp3)

*Experience how our AI agent interacts with customers in real-time conversations.*

---

## ✨ Features
- Dynamic AI voice calls powered by Retell.
- Personalized SMS follow-ups after calls.
- Scalable workflow adaptable to any business.
- End-to-end automation using n8n and Streamlit.

---

## 🧩 Tech Stack
| Component | Purpose |
|------------|----------|
| **Streamlit (Python)** | Frontend form for lead capture |
| **n8n** | Workflow automation and API integration |
| **Retell API** | AI voice calling and SMS follow-ups |
| **AI Agent** | Your branded AI assistant for client engagement |

---

## 🧠 Architecture
```
[Streamlit Form]
    ↓ (POST JSON)
[n8n Workflow]
    ├── Webhook/Form Trigger
    └── HTTP Request → Retell API
        ↓
[Agent Calls The User]
    ↓
[AI Agent Voice Call + SMS Follow-up]
```

---

## ⚙️ Setup Steps

### 1️⃣ Deploy Streamlit Form
1. Create a form to collect user details:
```python
import streamlit as st
import requests

st.title("Book a Call with Our AI Agent")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number (with country code)")
budget = st.text_input("Enter Budget")
subject = st.text_area("How can we assist you?")

if st.button("Submit"):
    data = {
        "Name": name,
        "Email": email,
        "Phone Number": phone,
        "Budget":budget
        "Subject": subject
    }
    response = requests.post("https://your-n8n-domain/webhook/ai-agent-form", json=data)
    if response.status_code == 200:
        st.success("Thank you! Our AI agent will reach out shortly.")
    else:
        st.error("Something went wrong. Please try again.")
```

2. Run your app:
```bash
streamlit run app.py
```

---

### 2️⃣ Configure n8n Workflow
1. Create a Webhook Node or Form Trigger to receive form submissions.
2. Connect it to an HTTP Request Node that calls Retell's API.
3. Add the JSON payload:
```json
{
  "from_number": "+14155550123",
  "to_number": "{{ $json['Phone Number'] }}",
  "retell_llm_dynamic_variables": {
    "name": "{{ $json.Name }}",
    "email": "{{ $json.Email }}",
    "phone number": "{{ $json['Phone Number'] }}",
    "budget": "{{ $json.Budget }}",
    "subject": "{{ $json.Subject }}"
  },
  "override_agent_id": "agent_your_business_001"
}
```
4. Add your Retell API Key as a Bearer Token in Headers.

---

### 3️⃣ Setup Retell Platform
1. Create your AI Agent (voice and persona).
2. Configure:
   - Virtual phone number (from_number)
   - Follow-up SMS message
   - API Key and Agent ID
3. Optionally enable call transcripts or callback webhooks to log call data.

---

## 📊 Supported Industries
| Industry | Example Use Case |
|----------|------------------|
| Real Estate | Follow up on property inquiries |
| Education | Contact students about courses |
| Finance | Onboard customers with AI support |
| Healthcare | Schedule patient appointments |
| SaaS | AI agent for demos and customer onboarding |

---

## 💼 Credits
Developed using **Streamlit**, **n8n**, and **Retell API**  
Designed to empower businesses to automate voice-based customer engagement with AI.
