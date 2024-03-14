#---PIP PACKAGES----#
import streamlit as st
from ApiNinjas import randomword
import requests

#---BUILT IN PYTHON PACKAGES----#
import secrets
import string

#---STREAMLIT SETTINGS---#
page_title = "PW & PW-Sentence Generator"
page_icon = ":building_construction:"
layout = "centered"

#---PAGE CONFIG---#
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

"#"
st.title(f"{page_icon} {page_title}")
"#"

#---STREAMLIT CONFIG HIDE---#
hide_st_style = """<style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

#---PW GENERATOR FUNCTION--#
def generate_pw()->None:
    letters = string.ascii_letters
    digits = string.digits  
    alphabet = letters + digits
    pwd_length = 15
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))


    st.session_state["pw"] = pwd

    #---PASSPHRASE GENERATOR FUNCTIONS---#

    #---GET RANDOM WORD---#
def get_random_word()->str:
    """Uses the API Ninja API to request a word string. 
       This string is then parsed to extract only the
       word and return it."""
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': st.secrets.API_NINJA})
    if response.status_code == requests.codes.ok:
        returned_word = response.text.split(":")
        returned_word = returned_word[1]
        returned_word  = returned_word[2:-2]
        return returned_word
    else:
        return "Error:", response.status_code, response.text
    
     #---GENERATING THE PHRASE---#
def generate_ps()->None:
    """Uses the get_random_word function to request five words. These are concatenated into a string with dashes and then
    assigned these to the session_state variable [pw] """
    passphrase = ""
    for x in range(5):
        passphrase += f"{get_random_word()}-"
    passphrase_final = passphrase[:-1]  
    st.session_state["pw"] = passphrase_final

    #---MAIN PAGE---#


if "pw" not in st.session_state:
    st.session_state["pw"] = ''
   
"---"

col1,col2 = st.columns([4,4], gap = "large")


with col1:
    st.caption("Secure password length is set at 15 chars.")
    st.button("Generate secure password", key = "pw_button", on_click = generate_pw)


with col2:
    st.caption("Secure passphrase length is set at 5 words.")
    st.button("Generate secure password sentence", key = "ps_button", on_click = generate_ps)
"#"
"#"

ocol1, ocol2, ocol3 = st.columns([1,4,1])
with ocol1:
    ''
with ocol2:
    st.caption("Generated secure password")
    "---"
    st.subheader(st.session_state["pw"])
    "---"
   
with ocol3:
    ''