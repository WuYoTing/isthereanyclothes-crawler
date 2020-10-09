import smtplib
from email.mime.text import MIMEText
import platform


def mail_log(mail_title, mail_content):
    # mail-info
    os_name = platform.system()
    if os_name == 'Linux':
        mail_info = open("/isthereanyclothes/mail-info.txt", "r")
    elif os_name == 'Windows':
        mail_info = open("E:\isthereanyclothes\mail-info.txt", "r")
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
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(mail_user, mail_password)
    server.send_message(mail_obj)
    server.quit()
    print(mail_title + 'sent!')
