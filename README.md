# AI Court Document Assistant (India - State Specific)

An AI-powered legal document suggestion assistant built using Python, Streamlit, and Google Gemini AI.

This application helps users identify the required legal documents for different types of court cases under Indian jurisdiction based on the selected state and case description.

---

# Features

- State-specific legal document suggestions
- Powered by Google Gemini AI
- Simple and interactive Streamlit UI
- Generates required document lists instantly
- 🇮🇳 Supports multiple Indian states

---

# Technologies Used

- Python
- Streamlit
- Google Gemini AI API

---

# Project Structure

```bash
AI-Court-Document-Assistant/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Court-Document-Assistant.git
```

## 2️⃣ Move into the Project Folder

```bash
cd AI-Court-Document-Assistant
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup Gemini API Key

Open the `app.py` file and replace:

```python
os.environ['GEMINI_API_KEY'] = "Your_openai_key"
```

with your actual Gemini API key:

```python
os.environ['GEMINI_API_KEY'] = "YOUR_GEMINI_API_KEY"
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# How It Works

1. Select your Indian state
2. Enter your legal case details
3. Click the Submit button
4. AI generates the list of required legal documents

---

# Example Use Case

### Input:
Property dispute between family members in Maharashtra.

### Output:
- Property ownership documents
- Identity proof
- Address proof
- Sale deed
- Encumbrance certificate
- Legal heir certificate

---

# 🔮 Future Improvements

- PDF export support
- Multi-language support
- Legal chatbot integration
- Court form auto-generation
- Lawyer recommendation system

---

# Disclaimer

This project is for educational and informational purposes only and should not be considered legal advice.

---

# Author

Vaibhav Bedre
