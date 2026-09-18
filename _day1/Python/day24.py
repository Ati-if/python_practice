from email.message import EmailMessage
import getpass
import smtplib
import ssl

# Email details
sender_email = "your_email@gmail.com"
# Use a 16-character Google App Password (not your normal password)
password = getpass.getpass("Enter your email app password: ")
receiver_email = "recipient@example.com"

# Build the email message
msg = EmailMessage()
msg["Subject"] = "Test Email via SSL"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.set_content("Hello! This email was sent using EmailMessage and SMTP_SSL.")

# Create secure SSL context
context = ssl.create_default_context()

try:
    # Connect to Gmail's SSL port
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully!")

except Exception as e:
    print(f"Error sending email: {e}")