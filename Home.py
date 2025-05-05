import streamlit as st

st.set_page_config(page_title="Multi-App", layout="centered")
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to switch pages.")

st.title("🏠 AI-powered Mindmap Creator")
st.subheader("Welcome to the AI mindmap Toolkit Homepage!")
st.image("images/app.1.jpg", use_container_width=True, caption="AI-generated Mindmap")
image_url = "https://drive.google.com/file/d/1g5pUd-fy-sRMtRJk4qfcHZPso6vj3dzU/view?usp=drive_link" 
st.image(image_url, caption="Donation for AI Mindmap app")
