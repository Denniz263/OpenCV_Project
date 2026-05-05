import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

SENDER_EMAIL = "dennizbek263@gmail.com"
SENDER_PASSWORD = "ublg fzep crqi ixtf"
RECEIVER_EMAIL = "dennizbek263@gmail.com"

def alert():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Motion Detected!"

    body = f"Motion was detected by your surveillance system at {timestamp}."
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Email error: {e}")

