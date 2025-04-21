# County Cricketer Lovers Membership Site

Welcome to the County Cricketer Lovers Membership Site! This Streamlit application provides exclusive access to cricket statistics and insights for members.

## Project Structure

```
county-cricketer-app
├── main.py          # Entry point for the Streamlit app
├── login.py         # Contains the login form and authentication logic
├── home.py          # Displays the public landing page
├── dashboard.py     # Member dashboard with embedded Power BI report
├── requirements.txt  # Lists project dependencies
└── README.md        # Documentation for the project
```

## Features

- **Member Login**: Secure login for members to access exclusive content.
- **Public Landing Page**: Information about membership and features available.
- **Power BI Dashboard**: Interactive dashboard with detailed cricket statistics and reports.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd county-cricketer-app
   ```

2. **Install Dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Streamlit app by running:
   ```
   streamlit run main.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.