import streamlit as st
import google.generativeai as genai
import os

# Set your Gemini API key
os.environ['GEMINI_API_KEY'] = "Your_openai_key"

# Configure Gemini AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit UI
st.title("📜 AI Court Document Assistant (India - State Specific)")
st.write("Describe your case, select your state, and I'll suggest the required documents as per Indian law!")

# Dropdown for state selection
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", 
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", 
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi", "Other (Central Laws)"
]

selected_state = st.selectbox("Select your state:", states)

# User Input
case_details = st.text_area("Enter details about your case:")

# Submit Button
if st.button("Submit"):
    if case_details.strip():
        # Send query to Gemini
        model = genai.GenerativeModel("models/gemini-2.0-pro-exp-02-05")
        response = model.generate_content(
            f"List only the required legal documents for the following case under Indian jurisdiction, "
            f"specific to {selected_state}:\n{case_details}\n"
            "Respond with only a bullet point list of document names, as per Indian legal requirements."
        )

        # Display AI-generated document list
        st.subheader(f"📄 Required Documents for {selected_state}:")
        st.write(response.text)
    else:
        st.warning("Please enter case details before submitting.")
