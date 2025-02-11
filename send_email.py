import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = "your_fake_email@example.com"
receiver_email = "victim@example.com"
subject = "Security Alert"
body = """Dear User,

Your account has been compromised. Please reset your password immediately by clicking here:

http://localhost:8080

Regards,
IT Support"""

# SMTP Server Configuration (use a disposable SMTP server)
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "your_fake_email@gmail.com"
smtp_password = "your_email_password"

# Setup email
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
