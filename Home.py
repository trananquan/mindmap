import streamlit as st
from st_paywall import add_auth

add_auth()
# Customized usage
add_auth(
    required=False,  # Don't stop the app for non-subscribers
    show_redirect_button=True,
    subscription_button_text="Get Premium Access!",
    button_color="#4CAF50",  # Green button
    use_sidebar=False  # Show button in main section
)

st.set_page_config(page_title="Multi-App", layout="centered")
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to switch pages.")

st.title("🏠 AI-powered Mindmap Creator")
st.subheader("Welcome to the AI mindmap Toolkit Homepage!")
st.image("images/app.1.jpg", use_container_width=True, caption="AI-generated Mindmap")
