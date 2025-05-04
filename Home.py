import streamlit as st
from st_paywall import add_auth

# Prevent access without payment
if not add_auth(
    required=True,  # Stop the app if user is not subscribed
    show_redirect_button=True,  # Show the subscription button
    subscription_button_text="Subscribe Now!",  # Custom button text
    button_color="#FF4B4B"
):
    st.stop()

st.set_page_config(page_title="Multi-App", layout="centered")
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to switch pages.")

st.title("🏠 AI-powered Mindmap Creator")
st.subheader("Welcome to the AI mindmap Toolkit Homepage!")
st.image("images/app.1.jpg", use_container_width=True, caption="AI-generated Mindmap")
