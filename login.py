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
            # Check if secrets are configured
            if "correct_username" not in st.secrets or "correct_password" not in st.secrets:
                st.sidebar.error("Login credentials not configured in secrets.toml.")
                # --- Debugging: Show what keys *are* present ---
                st.sidebar.caption(f"Available secret keys: {list(st.secrets.keys())}")
                # --- End Debugging ---
            # Validate against secrets
            elif username == st.secrets["correct_username"] and password == st.secrets["correct_password"]:
                st.session_state.logged_in = True
                st.session_state.username = username # Store username for display
                # st.success("Login successful!") # Success message is often better shown on the main page after rerun
                st.rerun()  # Rerun the app to reflect the logged-in state
            else:
                st.sidebar.error("Incorrect username or password.")