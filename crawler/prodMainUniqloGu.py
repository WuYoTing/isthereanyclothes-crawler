from getSeleniumPage import createDriverInstance
from crawler.prodListGu import getGuProd
from crawler.prodListUniqlo import getUniqloProd
from mail.mailLog import maillog
from datetime import date
import time


def prodMainUniqloGu(dbUserName, dbPassword):
    today_date = str(date.today())
    driver = createDriverInstance()
    # Gu
    gu_start_time = time.time()
    getGuProd(driver, dbUserName, dbPassword)
    gu_end_time = time.time()
    gu_total_time = gu_end_time - gu_start_time
    # Uniqlo
    uniqlo_start_time = time.time()
    getUniqloProd(driver, dbUserName, dbPassword)
    uniqlo_end_time = time.time()
    uniqlo_total_time = uniqlo_end_time - uniqlo_start_time
    driver.close()
    # gu total time
    gu_prod_time = round(gu_total_time, 2)
    m, s = divmod(gu_prod_time, 60)
    h, m = divmod(m, 60)
    gu_prod_info_total = "%02d:%02d:%02d" % (h, m, s)
    # uniqlo total time
    uniqlo_prod_time = round(uniqlo_total_time, 2)
    m, s = divmod(uniqlo_prod_time, 60)
    h, m = divmod(m, 60)
    uniqlo_prod_info_total = "%02d:%02d:%02d" % (h, m, s)
    # email msg
    mail_msg = 'GU 爬蟲使用時間 : ' + gu_prod_info_total + ' 秒  ' \
               + 'uniqlo 爬蟲使用時間 : ' + str(uniqlo_prod_info_total) + ' 秒 '

    maillog(today_date + ' 爬蟲完畢', mail_msg,
            'hakosaki314@gmail.com')
