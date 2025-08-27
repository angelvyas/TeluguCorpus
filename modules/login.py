import streamlit as st
import requests
from modules.swecha import login   
from modules.register import run as signup_page

def run():
    style = """
    <style>
    .reportview-container { background: linear-gradient(135deg, #00c6ff, #0072ff); height: 100vh;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .welcome-text { font-size: 3rem; font-weight: 700; color: white; margin-bottom: 30px;
        user-select: none; text-align: center; text-shadow: 1px 1px 5px rgba(0,0,0,0.4); }
    .auth-box { background: white; border-radius: 10px; padding: 40px 50px; max-width: 400px; width: 100%;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); }
    .powered { margin-top: 25px; font-size: 13px; color: #e0e0e0; user-select: none;
        font-family: monospace; text-align: center; text-shadow: 0 0 3px rgba(0,0,0,0.3); }
    a { color: #0072ff !important; text-decoration: none; } a:hover { text-decoration: underline; }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

    st.markdown('<div class="welcome-text">🔐 Welcome</div>', unsafe_allow_html=True)
    phone = st.text_input("Phone Number", key="login_phone")
    password = st.text_input("Password", type="password", key="login_password")
    st.markdown('<div class="powered">Powered by Swecha</div>', unsafe_allow_html=True)

    if st.button("Login", key="login_button"):
        try:
            resp = login(phone, password)
            if resp.status_code == 200:
                data = resp.json()
                st.write(data)
                token = data.get("access_token")
                if token:
                    st.session_state.logged_in = True
                    st.session_state.auth_token = token
                    st.success("Login successful! 🎉")
                    # st.rerun()
                else:
                    st.error("Login failed: No token returned.")
            else:
                st.error(f"Login failed: {_nice_error(resp)}")
        except requests.RequestException as e:
            st.error(f"Network error: {e}")

    # st.page_link("pages/Page1.py", label="👉 Go to Page 1")

