import streamlit as st
import requests
import time

from modules.meme_generator import run as meme_generator
from modules.prompt_collector import run as prompt_collector
# from story_classifier import story_classifier
# from voice2text import voice_to_text
# from offline_chatbot import offline_chatbot
# from meme_gallery import meme_gallery

from modules.login import run as login_page   

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Must be the very first Streamlit command
st.set_page_config(page_title="Telugu Tatvam", layout="centered")

# st.session_state.logged_in = True
# st.session_state.auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTYzOTYwMDMsInN1YiI6IjZlYWI4NGI2LTY5OWMtNDY1NC05NDVmLTgyNGViNzc4YmZmMiJ9.bz1lgksipThT1EhjXnF0w4JPHx40VrwJyn98zFjMJEs"

if not st.session_state.logged_in:
    login_page()    
else:
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio(
        "",
        [
            # "🧠 Values Vault",
            "🎙️ Prompt Collector",
            "🎭 Meme Generator",
            # "🎤 Voice to Text",
            # "💬 Assistant",
            # "🖼️ Meme Gallery",
        ],
    )

    if choice == "🎭 Meme Generator":
        meme_generator()
    # elif choice == "🧠 Values Vault":
    #     run_story_classifier()
    elif choice == "🎙️ Prompt Collector":
        prompt_collector()
    # elif choice == "🎤 Voice to Text":
    #     st.title("🎨 Meme Generator (Telugu Supported)")
    #     run_voice_to_text()
    # elif choice == "💬 Assistant":
    #     st.title("🎨 Meme Generator (Telugu Supported)")
    #     run_offline_chatbot()
    # elif choice == "🖼️ Meme Gallery":
    #     st.title("🎨 Meme Generator (Telugu Supported)")
    #     run_meme_gallery()