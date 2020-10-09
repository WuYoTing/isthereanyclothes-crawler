from crawler.prod_main import prod_main
import platform

os_name = platform.system()
print('os system : ' + os_name)
# database-info
if os_name == 'Linux':
    database_info = open("/isthereanyclothes/database-info.txt", "r")
elif os_name == 'Windows':
    database_info = open("D:\Python-workspace\database-info.txt", "r")
else:
    database_info = open("D:\database-info.txt", "r")
db_info_arr = database_info.readlines()

db_host = db_info_arr[0].strip('\n')
db_name = db_info_arr[1].strip('\n')
db_user_name = db_info_arr[2].strip('\n')
db_password = db_info_arr[3].strip('\n')
database_info.close()
# mail-info
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
#
prod_main(db_host, db_name, db_user_name, db_password, mail_user, mail_password, recipient)
