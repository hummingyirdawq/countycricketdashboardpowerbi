# filepath: c:\Users\rtayl\OneDrive\Rob Documents\Python Scripts\countycricketpowerbi\county-cricketer-app\main.py
import streamlit as st
from login import login_form
from home import home_page
from dashboard import dashboard_page
from bug_report import bug_report_page # Import the new page function

# --- Configuration ---
st.set_page_config(page_title="County Cricketer Stats", layout="wide")

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = 'home' # Default page

# --- Main App Logic ---

# Determine current page based on session state
current_page = st.session_state.page

if current_page == 'bug_report':
    bug_report_page()
elif st.session_state.logged_in:
    # If logged in, default to dashboard unless another page is explicitly set
    # This handles the case where user logs in and should go to dashboard
    if current_page != 'dashboard': # If page was set to something else before login, respect it? Or force dashboard?
         st.session_state.page = 'dashboard' # Force dashboard after login if not bug report
    dashboard_page()
    # Note: Login form is typically not shown when logged in, handled by sidebar logic now
else:
    # Not logged in, show home page and login form
    st.session_state.page = 'home' # Ensure page state is home
    home_page()
    login_form() # Display login form in the sidebar (as defined in login.py)