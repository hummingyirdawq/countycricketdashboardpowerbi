import streamlit as st
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    """Sends an email using SMTP."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server: # Use Gmail's SMTP server
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        return True # Indicate success
    except smtplib.SMTPAuthenticationError:
        st.error("SMTP Authentication Error: Check your email/password in secrets.")
        return False
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

def bug_report_page():
    """Displays the bug report form and handles submission."""
    st.title("🐞 Report a Bug")
    st.markdown("Found an issue? Please let us know by filling out the form below.")

    # --- Check for secrets ---
    required_secrets = ["email_sender", "email_password", "email_recipient"]
    if not all(s in st.secrets for s in required_secrets):
        st.error("Email configuration missing in secrets.toml. Cannot send bug reports.")
        st.warning("Please ask the app administrator to configure `email_sender`, `email_password`, and `email_recipient` in the Streamlit secrets.")
        # Optionally, display the form but disable submission, or just stop.
        # For simplicity here, we show the form but sending will fail later if secrets are missing.
        # A better approach might be to disable the form submit button.

    with st.form("bug_report_form", clear_on_submit=True):
        bug_subject = st.text_input("Subject / Brief Description", max_chars=100, placeholder="e.g., Filter not working on Batting page")
        bug_description = st.text_area("Detailed Description", placeholder="Please describe the bug in detail. What were you doing? What happened? What did you expect?")
        steps_to_reproduce = st.text_area("Steps to Reproduce (Optional)", placeholder="1. Go to...\n2. Click on...\n3. See error...")
        contact_email = st.text_input("Your Email (Optional)", placeholder="So we can contact you if needed")

        submitted = st.form_submit_button("Submit Bug Report")

        if submitted:
            # --- Validate required fields ---
            if not bug_subject or not bug_description:
                st.warning("Please fill in at least the Subject and Description fields.")
            else:
                # --- Attempt to send email only if secrets seem present ---
                 if all(s in st.secrets for s in required_secrets):
                    sender_email = st.secrets["email_sender"]
                    sender_password = st.secrets["email_password"]
                    recipient_email = st.secrets["email_recipient"] # Should be r.taylor289@gmail.com

                    email_subject = f"Bug Report: {bug_subject}"
                    email_body = f"""
Bug Report Received:

Subject: {bug_subject}
Description:
{bug_description}

Steps to Reproduce:
{steps_to_reproduce if steps_to_reproduce else 'Not provided'}

Contact Email: {contact_email if contact_email else 'Not provided'}
"""
                    # Send the email
                    success = send_email(
                        subject=email_subject,
                        body=email_body,
                        sender=sender_email,
                        recipients=[recipient_email],
                        password=sender_password
                    )

                    if success:
                        st.success("Thank you! Your bug report has been submitted successfully.")
                    # Error messages are handled within send_email
                 else:
                     # This case handles if secrets check passed initially but failed here (unlikely but safe)
                     st.error("Email configuration missing in secrets.toml. Cannot send bug report.")


    st.divider()
    # Button to go back - adjust target page based on where user came from if needed
    if st.button("⬅️ Back"): # Changed button text
         # Check if user was logged in to decide where to go back
        if st.session_state.get('logged_in', False):
             st.session_state.page = 'dashboard'
        else:
             st.session_state.page = 'home' # Or handle appropriately
        st.rerun()
