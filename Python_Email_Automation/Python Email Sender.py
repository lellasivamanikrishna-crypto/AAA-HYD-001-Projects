import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "lellasivamanikrishna@gmail.com"
app_password = "YOUR_APP_PASSWORD"

recipients = [
    "sivamani2006@gmail.com",
    "lsmk1809@gmail.com",
    "24HU1A42B9@rvit.edu"
]

subject = "Test Mail"
body = "This is a test mail. Please ignore it."

smtp_server = "smtp.gmail.com"
smtp_port = 587

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(sender_email, app_password)
    print("Login successful.")

    for recipient in recipients:
        email = MIMEMultipart()
        email["From"] = sender_email
        email["To"] = recipient
        email["Subject"] = subject

        email.attach(MIMEText(body, "plain"))

        server.sendmail(
            sender_email,
            recipient,
            email.as_string()
        )

        print(f"Email sent to {recipient}")

    server.quit()
    print("All emails sent successfully.")

except Exception as error:
    print("Something went wrong:", error)