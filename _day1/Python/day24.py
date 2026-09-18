from email.message import EmailMessage
import getpass
import smtplib
import ssl



def send_test_email():
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


if __name__ == "__main__":
    send_test_email()














import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    N = 30
    np.random.seed(10)
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))
    area = (30 * np.random.rand(N)) ** 2
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()







import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame(np.random.randn(6, 4), index=list(range(1, 7)), columns=list("ABCD"))
    print(df)
    print(df.describe())