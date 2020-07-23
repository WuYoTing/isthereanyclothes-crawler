from getSeleniumPage import createDriverInstance
from crawlerUniqoGu.prodListGu import getGuProd
from crawlerUniqoGu.prodListUniqlo import getUniqloProd
from sql_connector import test_sql
import getpass

userName = input('請輸入資料庫使用者名稱 : ');
password = getpass.getpass('請輸入資料庫密碼 : ');
if (test_sql(userName, password)):
    driver = createDriverInstance()
    # Gu
    getGuProd(driver, userName, password)
    # Uniqlo
    getUniqloProd(driver, userName, password)
    driver.close()
else:
    print('請重新啟動')
