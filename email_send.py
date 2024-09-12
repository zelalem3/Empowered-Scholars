import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'z88812586@gmail.com'
app_password = 'jkij szcm bfif shuk'

# Create the email content
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'zgetnet24@gmail.com'
msg['Subject'] = 'Subject Here'

# Body of the email
body = 'This is an email sent from Python!'
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(username, app_password)
    server.send_message(msg)
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
finally:
    server.quit()
