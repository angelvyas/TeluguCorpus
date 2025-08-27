import os
import json
import random
from datetime import datetime
import streamlit as st
import geocoder
from modules.swecha import get_categories, upload_file, get_current_user, upload_record

def run():
    
    st.title("🎙️ Corpus Collection")
    title = st.text_input("Title (Telugu supported)")
    description = st.text_input("Description (Telugu supported)")

    # Check length
    if description:
        if len(description) < 32:
            st.error("❌ Text must be at least 32 characters long.")
        else:
            st.success("✅ Valid input!")

    # Language options
    languages = {
        "english": "english",
        "hindi": "hindi",
        "telugu": "telugu",
        "tamil": "tamil",
        "gujarati": "gujarati",
        "bengali": "bengali",
        "marath": "marathi"
    }

    language = st.selectbox("Choose your language:", list(languages.keys()))
            
    # Location detection
    try:
        location_info = geocoder.ip('me')
        location = f"{location_info.city}, {location_info.country}" if location_info.ok else "Unavailable"
    except:
        location = "Unavailable"

    st.markdown(f"📍 **Your Location:** `{location}`")

    # Prompt selection
    categories = get_categories()
    prompt_categories = [(item["id"], item["name"]) for item in categories]
    selected_category = st.selectbox("📂 Select a Category", options=prompt_categories, format_func=lambda x: x[1])

    # Get the question based on category
    file_path = "modules/prompt_questions.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            questions = json.load(f) 
            prompt_cat_ques_list = questions[selected_category[1]]

    prompt_cat_ques = prompt_cat_ques_list[random.randint(0, len(prompt_cat_ques_list) -1 )]
    
    st.subheader("📝 Prompt")
    st.markdown(f"**{prompt_cat_ques}**")

    if st.button("🔄 Refresh Question"):
        st.rerun()

    # Submission Mode
    st.subheader("🔴 Recording/Typing")
    mode = st.radio("Submission Mode", ["Text","Audio", "Video", "Image"])

    if mode == "Text":
        text_response = st.text_area("Write your response here")
    elif mode == "Image":
        uploaded_file =  st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    elif mode == "Audio":
        uploaded_file =  st.file_uploader("Upload an Audio", type=["mp3"])
    elif mode == "Video":
        uploaded_file =  st.file_uploader("Upload an Video", type=["wav", "m4a", "mp4", "webm", "mkv"])

    if st.button("✅ Submit"):
        if mode in ["Audio", "Video","Image"] and not uploaded_file:
            st.error("Please upload your file.")
        elif mode == "Text" and not text_response.strip():
            st.error("Please write your response.")
        else:
            if mode in ["Audio", "Video","Image"]:
                # File upload 
                res = upload_file(uploaded_file)
                
                current_user = get_current_user()
                
                # Create the record json to upload the record 
                record = {
                    "title": title,
                    "description": description,
                    "category_id": selected_category[0],
                    "user_id": current_user["id"],
                    "media_type": "image",
                    "upload_uuid": res["upload_uuid"],
                    "filename": uploaded_file.name,
                    "total_chunks": 1,
                    "latitude": 0,
                    "longitude": 0,
                    "release_rights": "creator",
                    "language": language,
                    "use_uid_filename": False
                }
                
                res = upload_record(record)
                st.write(res)
                st.write(record)