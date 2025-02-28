
# Email content
subject = "Server Alert"
body = "This is an automated message from the server."

# Sender and recipient
sender_email = "rahmonbekmaqsudov4164@gmail.com"
receiver_email = "maqsudov_r@auca.kg"
password = "Teenwolf4164@$"

# Set up the MIMEText message
message = MIMEText(body)
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

# Send the email via Gmail's SMTP server (you can change this based on your mail server)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()
>>>>>>> aecdfbe (Add lab_7: Crontab and Python script for email automation)
