import os
import smtplib
from email.message import EmailMessage

def send_email_without_dependencies():
    # Retrieve sender, password, and recipient from environment variables
    # For Gmail, if 2FA is enabled, you'll need an 'App password' instead of your regular password.
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD") 
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    if not all([sender_email, sender_password, recipient_email]):
        print("Error: Please set SENDER_EMAIL, SENDER_PASSWORD, and RECIPIENT_EMAIL environment variables.")
        print("For Gmail, generate an 'App password' if 2FA is enabled: myaccount.google.com/apppasswords")
        return

    # Define email content
    subject = "Python Standard Library Email Test"
    body = "This email was sent using only Python's standard library (smtplib and email.message)!"

    # Create the email message object using email.message.EmailMessage
    # This is the modern and recommended way to construct email messages.
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.set_content(body) # Set the plain text content of the email

    # SMTP server details (e.g., for Gmail's SMTP server)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587 # Standard port for TLS (STARTTLS)

    try:
        # Establish a connection with the SMTP server
        # smtplib.SMTP creates an SMTP client instance.
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Upgrade the connection to a secure encrypted TLS connection
            # This is crucial for secure communication over port 587.
            server.starttls()
            # Log in to the SMTP server with the sender's credentials
            server.login(sender_email, sender_password)
            # Send the email message. send_message handles all MIME formatting.
            server.send_message(msg)
            print(f"Email successfully sent from {sender_email} to {recipient_email}!")
    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP authentication failed. Check your SENDER_EMAIL and SENDER_PASSWORD.")
        print("Remember to use an 'App password' for Gmail if 2FA is enabled.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    send_email_without_dependencies()
