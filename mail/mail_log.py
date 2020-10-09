import smtplib
from email.mime.text import MIMEText


def mail_log(mail_user, mail_password, recipient, mail_title, mail_content):
    # mail-info
    mail_obj = MIMEText(mail_content)
    mail_obj['Subject'] = mail_title
    mail_obj['From'] = mail_user
    mail_obj['To'] = recipient
    try:
        smtp = smtplib.SMTP('smtp.gmail.com')
        smtp.ehlo()
        smtp.starttls()
        smtp.login(mail_user, mail_password)
        smtp.send_message(mail_obj)
        smtp.quit()
        print(mail_title + ' sent! ')
    except smtplib.SMTPException:
        pass
    except smtplib.socket.error:
        pass
