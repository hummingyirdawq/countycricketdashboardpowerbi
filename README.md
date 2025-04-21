# County Cricketer Lovers Membership Site 🏏

Welcome to the County Cricketer Lovers Membership Site! This Streamlit application provides exclusive access to detailed cricket statistics and insights for members via an embedded Power BI dashboard.

## Project Structure

```
county-cricketer-app/
├── app.py           # Main Streamlit application script (or main.py)
├── login.py         # Handles user authentication using Streamlit secrets
├── home.py          # Defines the content for the public landing page
├── dashboard.py     # Defines the content for the members-only dashboard page
├── .streamlit/
│   └── secrets.toml # Stores credentials and configuration (!!! MUST NOT BE COMMITTED TO GIT !!!)
├── requirements.txt # Lists Python dependencies for the project
├── .gitignore       # Specifies intentionally untracked files (like secrets.toml)
└── README.md        # This documentation file
```
*(Note: Ensure your main script is named `app.py` or update the structure above)*

## Architecture

This application utilizes a simple yet effective architecture:

1.  **Frontend Framework**: [Streamlit](https://streamlit.io/) is used to create the interactive web application interface, handle user sessions, and manage page navigation.
2.  **Authentication**: User login is managed via Streamlit's built-in `st.secrets`. Credentials (`correct_username`, `correct_password`) are stored securely in a `secrets.toml` file (either locally in `.streamlit/` or in the Streamlit Cloud environment settings) and are *not* committed to the Git repository thanks to `.gitignore`. The `login.py` module handles the form presentation and validation logic.
3.  **Data Visualization**: The core statistical data is presented through an embedded [Microsoft Power BI](https://powerbi.microsoft.com/) report. The `dashboard.py` module contains the `iframe` code to embed the report securely.
4.  **Deployment**: The application is designed to be deployed on [Streamlit Community Cloud](https://streamlit.io/cloud), which handles hosting, scaling, and secret management in production.

## How it Works

1.  **Initialization**: When a user accesses the app, `app.py` (or `main.py`) runs. It checks the `st.session_state` to see if the user is already logged in (`st.session_state.logged_in`).
2.  **Public View**: If the user is not logged in, the application displays the public landing page content defined in `home.py` and presents the login form (from `login.py`) in the sidebar.
3.  **Login Attempt**: The user enters their credentials into the sidebar form. Upon submission, `login.py` compares the input against the credentials stored in `st.secrets` (handling both local and deployed secret structures).
4.  **Authentication Success**: If the credentials match, `st.session_state.logged_in` is set to `True`, and `st.rerun()` is called to reload the application state.
5.  **Member View**: Now that `st.session_state.logged_in` is `True`, `app.py` displays the member dashboard content defined in `dashboard.py`. This includes the title, welcome message, and the embedded Power BI `iframe`. A logout button is also displayed in the sidebar.
6.  **Logout**: Clicking the logout button sets `st.session_state.logged_in` back to `False` and triggers `st.rerun()`, returning the user to the public view.

## Features & Membership 📚

This site provides members access to:

*   🏏 **County Championship Ultimate Database**: An extensive Power BI report.
*   📊 **Extensive Player Statistics**: Covering records from 1890-2024.
*   📈 **Detailed Ball-by-Ball Records**: Available for the years 2020-2024.
*   🎯 **Player Stats vs. Bowling Types**: Analyze performance against different bowling styles.
*   🆚 **Batter vs. Bowling Matchups**: Detailed head-to-head statistics.
*   🏆 **Player Rankings**: See how players stack up.
*   👉 **Cricket Captain 2024 Stats Pack**: Join the community stats pack.

### How to Access

*   **Already a Member?** Use the login details provided via the BuyMeACoffee County Cricket posts. Enter them in the sidebar login form.
*   **New Here?** Sign up to the **County Cricketer Lover** tier at [https://buymeacoffee.com/leadingedgepod](https://buymeacoffee.com/leadingedgepod) to receive login credentials and gain access.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.