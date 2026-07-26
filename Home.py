import streamlit as st

st.set_page_config(
    page_title="AI Mindmap App",
    page_icon="🏠",
    layout="centered"
)

#==========================
# USER ACCOUNT
#==========================

USERNAME = st.secrets["USERNAME"]
PASSWORD = st.secrets["PASSWORD"]

#==========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():

    st.title("🔐 AI Mindmap Creator App")
    st.markdown("### Log in")
    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Log in"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Incorrect username or password.")

def home():

    st.sidebar.title("Navigation")
    st.sidebar.info(
        "Use the sidebar to switch pages."
    )
    if st.sidebar.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()
    st.markdown(
        "<h1 style='color: darkblue;'>🏠 AI-powered Mindmap Creator</h1>",
        unsafe_allow_html=True,
    )

    st.subheader(
        "Welcome to the AI Mindmap Toolkit Homepage!"
    )

    st.image(
        "images/app.1.jpg",
        use_container_width=True,
        caption="AI-generated Mindmap",
    )


if st.session_state.logged_in:
    home()
else:
    login()

st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: blue;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        div.stButton > button:hover {
            background-color: #002244;
        }
        </style>
        """,
        unsafe_allow_html=True
)
