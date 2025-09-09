import smtplib
from email.mime.text import MIMEText

def smtp_client():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "toletibharat@gmail.com"
    password = "**** **** **** ****"
    receiver_email = "gondianirudh15@gmail.com"

    # Create the email message
    message_subject = "CN Lab 2 SMTP Test"
    message_body = "This is a test email sent from a Python script for the SMTP assignment."
    msg = MIMEText(message_body)
    msg['Subject'] = message_subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    print("--- Starting SMTP Communication ---")
    try:
        # Connect to the server
        with smtplib.SMTP(smtp_server, port) as server:
            print(f"Connecting to {smtp_server}...")
            server.starttls() # Secure the connection
            print("Connection secured with TLS.")
            
            server.login(sender_email, password)
            print(f"Logged in as {sender_email}.")
            
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email sent successfully to {receiver_email}.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("--- SMTP Communication Finished ---")


if __name__ == "__main__":
    smtp_client()