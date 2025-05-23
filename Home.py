import streamlit as st

st.set_page_config(page_title="Multi-App",page_icon="🏠", layout="centered")
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to switch pages/ Sử dụng thanh công cụ để chuyển giữa các App.")

st.markdown("<h1 style='color: darkblue;'>🏠 AI-powered Mindmap Creator</h1>", unsafe_allow_html=True)
st.subheader("Welcome to the AI mindmap Toolkit Homepage!")
st.image("images/app.1.jpg", use_container_width=True, caption="AI-generated Mindmap")
st.subheader("Donation/ Tài trợ")
st.write("Donation for AI Mindmap app. Apply for Vietnamese bank account (180.000 VND ~ 7$)")
st.write("Xin hãy tài trợ cho app để hoàn thiện thêm tính năng. Áp dụng cho tài khoản ngân hàng Việt Nam (180.000 VND ~ 7$)")
st.image("images/Bidv_QR.jpg", width=300)
