import streamlit as st
import os # Import os

# --- Credentials from Secrets ---
# Load credentials from st.secrets (secrets.toml file)
# Ensure your secrets.toml has:
# correct_username = "YOUR_USERNAME"
# correct_password = "YOUR_PASSWORD"

def login_form():
    """Displays the login form in the sidebar."""
    st.sidebar.header("Member Login")

    # --- Optional Debugging: Check if secrets file exists ---
    # secrets_path_root = "secrets.toml"
    # secrets_path_subdir = os.path.join(".streamlit", "secrets.toml")
    # if not os.path.exists(secrets_path_root) and not os.path.exists(secrets_path_subdir):
    #     st.sidebar.warning("secrets.toml not found in root directory or .streamlit/ subdirectory.")
    # --- End Debugging ---

    with st.sidebar.form("login_form"):
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        submitted = st.form_submit_button("Login")

        if submitted:
            # Determine correct username and password based on secrets structure
            correct_username = None
            correct_password = None

            # Check for nested structure (like Streamlit Cloud)
            if "credentials" in st.secrets and \
               "correct_username" in st.secrets["credentials"] and \
               "correct_password" in st.secrets["credentials"]:
                correct_username = st.secrets["credentials"]["correct_username"]
                correct_password = st.secrets["credentials"]["correct_password"]
            # Check for flat structure (like local secrets.toml)
            elif "correct_username" in st.secrets and "correct_password" in st.secrets:
                correct_username = st.secrets["correct_username"]
                correct_password = st.secrets["correct_password"]

            # Validate credentials if found
            if correct_username is not None and correct_password is not None:
                if username == correct_username and password == correct_password:
                    st.session_state.logged_in = True
                    st.session_state.username = username # Store username for display
                    st.rerun()  # Rerun the app to reflect the logged-in state
                else:
                    st.sidebar.error("Incorrect username or password.")
            else:
                # Secrets not configured correctly in either structure
                st.sidebar.error("Login credentials not configured correctly in secrets.")
                # --- Debugging: Show available keys ---
                st.sidebar.caption(f"Available secret keys: {list(st.secrets.keys())}")
                if "credentials" in st.secrets:
                     st.sidebar.caption(f"Keys under 'credentials': {list(st.secrets['credentials'].keys())}")
                # --- End Debugging ---