#---PIP PACKAGES----#
import streamlit as st
import requests

#---BUILT IN PYTHON PACKAGES----#
import secrets
import string

#---STREAMLIT SETTINGS---#
page_title = "PyCryptPass - A simple yet effective Password and Passphrase Generator focused on cryptographic security."
page_icon = ":shushing_face:"
layout = "centered"

#---PAGE CONFIG---#
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

#---CUSTOM CSS STYLING---#
st.markdown("""
    <style>
        body {
            background-color: #f0f2f5;
            font-family: Arial, sans-serif;
        }
        .main {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0);
        }
        h1 {
            color: #ffffff
        }
        button {
            background-color: #007BFF;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .subheader {
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

#---PAGE TITLE---#
st.title(f"{page_icon} {page_title}")

#---STREAMLIT CONFIG HIDE---#
hide_st_style = """<style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

#---PW GENERATOR FUNCTION---#
def generate_pw() -> None:
    letters = string.ascii_letters
    digits = string.digits  
    alphabet = letters + digits
    pwd_length = 15
    pwd = ''.join(secrets.choice(alphabet) for _ in range(pwd_length))
    st.session_state["pw"] = pwd

#---GET RANDOM WORD---#
def get_random_word() -> str:
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    api_key = st.secrets["API_NINJA"]["key"]
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        returned_word = response.json().get("result", "Unknown")
        return returned_word
    else:
        st.error(f"Error: {response.status_code}, {response.text}")  
        return "Unknown"

#---GET RANDOM PASSPHRASE CONTENT---#
def get_random_passphrase() -> str:
    api_url = 'https://api.api-ninjas.com/v1/passphrase'  # Ensure this endpoint is correct
    api_key = st.secrets["API_NINJA"]["key"]
    
    # Make the API request
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    # Check if the response contains the expected key
    try:
        returned_passphrase = response.json().get("result", "WPTXpVO dlrY Rgydf KlEk kdrCOd")  # Adjust based on the actual key
        return returned_passphrase
    except (ValueError, requests.exceptions.RequestException) as e:
        st.error(f"Error: {e}")
        st.session_state["pw"] = "WPTXpVO dlrY Rgydf KlEk kdrCOd"  # Set a default value in case of error
        return "WPTXpVO dlrY Rgydf KlEk kdrCOd"
#---PASS PHRASE GENERATOR FUNCTION---#
def generate_ps() -> None:
    passphrase = get_random_passphrase()  # Fetch a random passphrase
    st.session_state["pw"] = passphrase  # Store the returned passphrase

#---MAIN PAGE---#
if "pw" not in st.session_state:
    st.session_state["pw"] = ''

st.markdown("---")

col1, col2 = st.columns([4, 4], gap="large")

with col1:
    st.caption("Secure password length is set at 15 chars.")
    st.button("Generate Secure Password", key="pw_button", on_click=generate_pw)

with col2:
    st.caption("Secure passphrase length is set at 5 words.")
    st.button("Generate Secure Passphrase", key="ps_button", on_click=generate_ps)

st.markdown("---")

#---OUTPUT DISPLAY---#
ocol1, ocol2, ocol3 = st.columns([1, 4, 1])
with ocol1:
    ''
with ocol2:
    st.caption("Generated Secure Output")
    st.markdown("---")
    st.subheader(st.session_state["pw"])
    st.markdown("---")
with ocol3:
    ''