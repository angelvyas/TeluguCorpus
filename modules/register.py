import streamlit as st
from datetime import date

def run():
    st.subheader("📝 Sign Up")

    full_name = st.text_input("Full Name", key="signup_full_name")
    phone = st.text_input("Phone Number", key="signup_phone")
    email = st.text_input("Email Address", key="signup_email")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="signup_gender")
    dob = st.date_input("Date of Birth", key="signup_dob", min_value=date(1900, 1, 1))
    place = st.text_input("Place", key="signup_place")
    password = st.text_input("Create Password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
    tos = st.checkbox("I agree to the Terms of Service and Privacy Policy", key="signup_tos")

    if st.button("Sign Up", key="signup_button"):
        if not tos:
            st.error("You must agree to the Terms of Service to continue.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.success("Signup successful! 🎉")