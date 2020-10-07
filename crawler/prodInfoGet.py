import sys
import datetime

sys.path.append("..")
from sql_connector.sql_connector import sql_connector
from getSeleniumPage import getSeleniumPage


def getProdInfo(prod_url, driver, tableName, userName, password):
    now = datetime.datetime.now()
    try:
        page = getSeleniumPage(prod_url, driver)
    except Exception as ec:
        raise
    prod_sex_category = page.select('#content #prodInfo .pathdetail')[0].text
    prod_sex = prod_sex_category.split(' ⁄ ')[0].strip()
    if prod_sex == "MEN":
        prod_sex = 1
    elif prod_sex == "WOMEN":
        prod_sex = 2
    else:
        prod_sex = 0
    prod_category = prod_sex_category.split(' ⁄ ')[1].strip()
    prod_name = page.select('#content #prodInfo #goodsNmArea')[0].text
    # 未處理千元小數點問題
    prod_price = page.select('#content #prodInfo #basic #price')[0].text.replace('NT$', '').replace(',', '')
    prod_number = page.select('#content #prodInfo #basic .number')[0].text.replace('商品編號', '')
    prod_about = page.select('#content #secondary #prodDetail .content .about')[0].text
    prod_material = page.select('#content #secondary #prodDetail .content .spec dd')[0].text
    prod_main_image_url = page.select('#content #secondary #prodMainImg #prodImgDefault')[0].img['src'].replace(
        'model', '').replace('_.jpg', '.jpg')
    try:
        prod_size_url = page.select('#content #prodSelectAttribute #prodSelectSize #selectSizeDetail .linkMore a')[
            0].get(
            'href')
        prod_size_url = prod_size_url.replace("javascript:void(window.open('", "")
        prod_size_url = prod_size_url.replace(
            "', '', 'width=600, height=700, status=no, toolbar=no, menubar=no, location=no, resizable=yes, "
            "scrollbars=yes'));", "")
    except:
        prod_size_url = ""
    prod_isnewGood = page.findAll("li", {"id": "newGood"})[0].get('style')
    prod_isonlineOnly = page.findAll("li", {"id": "onlineOnlyIcon"})[0].get('style')
    prod_isSet = page.findAll("li", {"id": "Set"})[0].get('style')
    prod_islimitedTime = page.findAll("li", {"id": "limitedTime"})[0].get('style')
    prod_ispriceDown = page.findAll("li", {"id": "priceDown"})[0].get('style')
    prod_canmodify = page.findAll("li", {"id": "modifyShow"})[0].get('style')
    if prod_isnewGood == "display: none;":
        prod_isnewGood = 0
    else:
        prod_isnewGood = 1
    if prod_isonlineOnly == "display: none;":
        prod_isonlineOnly = 0
    else:
        prod_isonlineOnly = 1
    if prod_isSet == "display: none;":
        prod_isSet = 0
    else:
        prod_isSet = 1
    if prod_islimitedTime == "display: none;":
        prod_islimitedTime = 0
    else:
        prod_islimitedTime = 1
        prod_limitedPriceText = page.select('#content #prodInfo #goodsIconList #limitedTime #limitedPriceText')[
            0].text.replace(
            '止期間限定特價中', '')
        prod_limitedPriceMonthDay = prod_limitedPriceText.replace('/', '-')
        prod_limitedPriceDate = str(now.year) + '-' + prod_limitedPriceMonthDay
    if prod_ispriceDown == "display: none;":
        prod_ispriceDown = 0
    else:
        prod_ispriceDown = 1
    if prod_canmodify == "display: none;":
        prod_canmodify = 0
    else:
        prod_canmodify = 1
    # 這裡抓本地時間做string
    prod_get_time = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    if 'prod_limitedPriceDate' not in globals():
        prod_limitedPriceDate = None
    '''
    print(prod_sex)
    print(prod_category)
    print(prod_name)
    print(prod_price)
    print(prod_number)
    print(prod_about)
    print(prod_material)
    print(prod_url)
    print(prod_main_image_url)
    print(prod_size_url)
    print(prod_isnewGood)
    print(prod_isonlineOnly)
    print(prod_isSet)
    print(prod_islimitedTime)
    print(prod_ispriceDown)
    print(prod_canmodify)
    print(prod_get_time)
    print(prod_limitedPriceDate)
    '''
    sql_connector(prod_sex, prod_category, prod_name, int(prod_price), prod_number, prod_about, prod_material, prod_url,
                  prod_main_image_url, prod_size_url, prod_isnewGood, prod_isonlineOnly, prod_isSet, prod_islimitedTime,
                  prod_ispriceDown, prod_canmodify, prod_limitedPriceDate, prod_get_time, tableName, userName, password)
