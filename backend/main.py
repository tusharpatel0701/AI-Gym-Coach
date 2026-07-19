import streamlit as st
from services.auth.login_wall import render_login_wall

st.set_page_config(page_title="AI GYM Coach")

def main():
    st.set_page_config(page_title="AI GYM Coach", page_icon="🏋️‍♂️", layout="centered", initial_sidebar_state="expanded")

    if not render_login_wall():
        return
    

if __name__ == "__main__":
    main()
