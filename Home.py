import streamlit as st

st.set_page_config(page_title="Multi-App", layout="centered")
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to switch pages.")

st.markdown("<h1 style='color: darkblue;'>🏠 AI-powered Mindmap Creator</h1>", unsafe_allow_html=True)
st.subheader("Welcome to the AI mindmap Toolkit Homepage!")
st.image("images/app.1.jpg", use_container_width=True, caption="AI-generated Mindmap")
st.subheader("Donation")
st.write("Donation for AI Mindmap app. Apply for Vietnamese banking account (100.000 VND ~ 4$)")
st.image("images/Bidv_QR.jpg", width=300)
