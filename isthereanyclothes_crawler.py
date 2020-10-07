from crawler.prodMainUniqloGu import prodMainUniqloGu
import platform

osName = platform.system();
print('os system : ' + osName)
# database-info
if osName == 'Linux':
    databaseInfo = open("/isthereanyclothes/database-info.txt", "r")
elif osName == 'Windows':
    databaseInfo = open("E:\isthereanyclothes\database-info.txt", "r")
dbInfoArr = databaseInfo.readlines()
dbUserName = dbInfoArr[0].strip('\n')
dbPassword = dbInfoArr[1].strip('\n')
databaseInfo.close()
prodMainUniqloGu(dbUserName, dbPassword)
