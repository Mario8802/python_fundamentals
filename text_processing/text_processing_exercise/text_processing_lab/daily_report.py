import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email configuration
    from_email = "your_email@gmail.com"
    to_email = "recipient_email@gmail.com"
    subject = "Daily Report"
    message = "This is your daily report."

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_email@gmail.com"
    smtp_password = "your_password"

    # Create message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send email
    server.send_message(msg)
    server.quit()

    print("Report sent successfully.")

# Schedule the task to run daily at a specific time
schedule.every().day.at("08:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep for 1 minute
