import smtplib
from email.mime.text import MIMEText
import platform


def mail_log(mail_title, mail_content):
    # mail-info
    os_name = platform.system()
    if os_name == 'Linux':
        mail_info = open("/isthereanyclothes/mail-info.txt", "r")
    elif os_name == 'Windows':
        mail_info = open("D:\Python-workspace\mail-info.txt", "r")
    else:
        mail_info = open("D:\mail-info.txt", "r")
    mail_info_arr = mail_info.readlines()
    mail_user = mail_info_arr[0].strip('\n')
    mail_password = mail_info_arr[1].strip('\n')
    recipient = mail_info_arr[2].strip('\n')
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
