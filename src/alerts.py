import smtplib
from email.message import EmailMessage

def send_alert(email, message):
    sender_email = "your-email@gmail.com"
    sender_password = "your-app-password"

    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "Crop Monitoring Alert"
    msg["From"] = sender_email
    msg["To"] = email

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send alert: {e}")

if __name__ == "__main__":
    send_alert("farmer@example.com", "Your crop is showing signs of disease. Immediate action required!")
