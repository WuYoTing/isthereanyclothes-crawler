import smtplib
from email.mime.text import MIMEText


def maillog(gmailUser, gmailPassword, gmailTitle, gmailContent, recipient):
    gmail_user = gmailUser
    gmail_password = gmailPassword  # your gmail password
    msg = MIMEText(gmailContent)
    msg['Subject'] = gmailTitle
    msg['From'] = gmail_user
    msg['To'] = recipient
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    print('Email sent!')