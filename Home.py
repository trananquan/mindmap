import streamlit as st
from st_paywall import add_auth

st.title("My Subscription App")

if not st.experimental_user.is_logged_in:
    st.write("Please log in to access this app")
    if st.button("Log in"):
        st.login()
else:
    add_auth(required=True)
    st.write("Welcome to the premium content!")

st.set_page_config(page_title="Multi-App", layout="centered")
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to switch pages.")

st.title("🏠 AI-powered Mindmap Creator")
st.subheader("Welcome to the AI mindmap Toolkit Homepage!")
st.image("images/app.1.jpg", use_container_width=True, caption="AI-generated Mindmap")
