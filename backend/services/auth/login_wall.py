import streamlit as st

# Fake database
FAKE_USERS = {
    "tushar": {
        "id": 1,
        "username": "tushar"
    },
    "prince": {
        "id": 2,
        "username": "prince"
    },
    "john": {
        "id": 3,
        "username": "john"
    }
}


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    st.title("🏋️‍♂️ AI Real-time GYM Trainer")
    st.markdown("### Welcome! Please enter a username to start.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "Name",
            placeholder="tushar / prince / john"
        )

        submit_button = st.form_submit_button(
            "Start Session",
            width="stretch"
        )

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False

        username = username.lower().strip()

        if username not in FAKE_USERS:
            st.error("User not found.")
            return False

        user = FAKE_USERS[username]

        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]

        st.success("Login Successful!")
        st.rerun()

    return False