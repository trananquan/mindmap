import streamlit as st
from st_paywall import add_auth

# Prevent access without payment
if not add_auth(
    stripe_public_key="pk_test_yourStripePublicKeyHere",   # Replace with your real Stripe public key
    product_price_id="price_1YourStripePriceID",           # Replace with your actual Stripe price ID
    title="🔐 Unlock the Mindmap App",
    text="Pay once to unlock full access to our AI-powered Mindmap Creator.",
):
    st.stop()

st.set_page_config(page_title="Multi-App", layout="centered")
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to switch pages.")

st.title("🏠 AI-powered Mindmap Creator")
st.subheader("Welcome to the AI mindmap Toolkit Homepage!")
st.image("images/app.1.jpg", use_container_width=True, caption="AI-generated Mindmap")
