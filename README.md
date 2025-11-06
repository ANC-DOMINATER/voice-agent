# Customer Enquiry Form - Streamlit App

A modern, responsive Streamlit application that embeds an n8n form for customer enquiries.

## Features

- 🎨 Modern gradient design with glassmorphism effects
- 📱 Fully responsive layout
- 🚀 Easy to deploy and customize
- 🔗 Seamlessly integrates n8n forms

## Setup Instructions

### 1. Create a Python Virtual Environment

```powershell
# Navigate to the project directory
cd "e:\DOM Dev\quantum leap"

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the Application

```powershell
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Configuration

To use your own n8n form, edit the `app.py` file and replace the iframe URL:

```python
src="https://n8n.yourdomain.com/forms/customer-enquiry"
```

with your actual n8n form URL.

## Customization

You can customize the following in `app.py`:

- **Colors**: Modify the gradient in the CSS section
- **Page Title**: Change the `page_title` in `st.set_page_config()`
- **Header Text**: Update the header section markdown
- **Form Height**: Adjust the `height` attribute in the iframe

## Deployment

This app can be deployed to:
- Streamlit Cloud (free)
- Heroku
- AWS
- Azure
- Any Python-compatible hosting service

## Requirements

- Python 3.8 or higher
- Streamlit 1.39.0

## License

MIT License
