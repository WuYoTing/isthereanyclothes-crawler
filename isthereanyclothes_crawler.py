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
db_user_name = db_info_arr[0].strip('\n')
db_password = db_info_arr[1].strip('\n')
database_info.close()
prod_main(db_user_name, db_password)
