from getSeleniumPage import createDriverInstance
from crawlerUniqoGu.prodListGu import getGuProd
from crawlerUniqoGu.prodListUniqlo import getUniqloProd

driver = createDriverInstance()
# Gu
getGuProd(driver)
# Uniqlo
getUniqloProd(driver)
driver.close()
