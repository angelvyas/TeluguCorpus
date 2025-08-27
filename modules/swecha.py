import requests
import uuid
import json
import streamlit as st

API_BASE = "https://api.corpus.swecha.org/api/v1"
REQ_TIMEOUT = 15  # seconds

def _auth_headers():
    token = st.session_state.get("auth_token")
    return {"Authorization": f"Bearer {token}"} if token else {}

def login(phone, password):
    payload = {"phone": phone, "password": password}
    return requests.post(f"{API_BASE}/auth/login", json=payload, timeout=REQ_TIMEOUT)

def get_current_user():
    try:
        resp = requests.get(f"{API_BASE}/auth/me", headers=_auth_headers(), timeout=REQ_TIMEOUT)
        if resp.status_code == 200:
            return resp.json()
        else:
            st.error(f"Failed to fetch user: {_nice_error(resp)}")
            return []
    except requests.RequestException as e:
        st.error(f"Network error while fetching categories: {e}")
        return []

def get_categories():
    try:
        resp = requests.get(f"{API_BASE}/categories/", headers=_auth_headers(), timeout=REQ_TIMEOUT)
        if resp.status_code == 200:
            return resp.json()
        else:
            st.error(f"Failed to fetch categories: {resp}")
            return []
    except requests.RequestException as e:
        st.error(f"Network error while fetching categories: {e}")
        return []

def upload_record(record):
    try:
        headers = _auth_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        resp = requests.post(f"{API_BASE}/records/upload", headers=headers, data=record)
        if resp.status_code == 200:
            return resp.json()
        else:
            st.error(f"Failed to upload record: {resp}")    
            return []
    except requests.RequestException as e:
        st.error(f"Network error while uploading record: {e}")
        return []

def upload_file(file):
    try:

        f_uuid = str(uuid.uuid4())
        headers = _auth_headers()
        headers["accept"] = "application/json"

        payload = {
            "filename": file.name,
            "chunk_index": 0,
            "total_chunks": 1,  
            "upload_uuid": f_uuid
        }

        files = { "chunk": (file.name, file.getvalue(), file.type)}

        # st.write(headers)
        # st.write(data)
        # st.write(files)

        resp = requests.post(f"{API_BASE}/records/upload/chunk", headers=headers, data=payload, files=files)
        if resp.status_code == 200:
            return resp.json()
        else:
            st.error(f"Failed to fetch categories: {resp}")
            return []
    except requests.RequestException as e:
        st.error(f"Network error while fetching categories: {e}")
        return []



