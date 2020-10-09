import datetime
from sql_connector.sql_connector import sql_connector
from get_selenium_page import get_selenium_page


def get_prod_info(prod_url, driver, table_name, user_name, password):
    now = datetime.datetime.now()
    try:
        page = get_selenium_page(prod_url, driver)
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
        prod_size_url = ""
        prod_is_newgood = page.findAll("li", {"id": "newGood"})[0].get('style')
        prod_is_onlineonly = page.findAll("li", {"id": "onlineOnlyIcon"})[0].get('style')
        prod_is_isset = page.findAll("li", {"id": "Set"})[0].get('style')
        prod_is_limitedtime = page.findAll("li", {"id": "limitedTime"})[0].get('style')
        prod_is_pricedown = page.findAll("li", {"id": "priceDown"})[0].get('style')
        prod_can_modify = page.findAll("li", {"id": "modifyShow"})[0].get('style')
        if prod_is_newgood == "display: none;":
            prod_is_newgood = 0
        else:
            prod_is_newgood = 1
        if prod_is_onlineonly == "display: none;":
            prod_is_onlineonly = 0
        else:
            prod_is_onlineonly = 1
        if prod_is_isset == "display: none;":
            prod_is_set = 0
        else:
            prod_is_set = 1
        if prod_is_limitedtime == "display: none;":
            prod_is_limitedtime = 0
        else:
            prod_is_limitedtime = 1
            prod_limited_price_text = page.select('#content #prodInfo #goodsIconList #limitedTime #limitedPriceText')[
                0].text.replace(
                '止期間限定特價中', '')
            prod_limited_price_month_day = prod_limited_price_text.replace('/', '-')
            prod_limited_price_date = str(now.year) + '-' + prod_limited_price_month_day
        if prod_is_pricedown == "display: none;":
            prod_is_pricedown = 0
        else:
            prod_is_pricedown = 1
        if prod_can_modify == "display: none;":
            prod_can_modify = 0
        else:
            prod_can_modify = 1
        # 這裡抓本地時間做string
        prod_get_time = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        if 'prod_limited_price_date' not in globals():
            prod_limited_price_date = None
        sql_connector(prod_sex, prod_category, prod_name, int(prod_price), prod_number, prod_about, prod_material,
                      prod_url, prod_main_image_url, prod_size_url, prod_is_newgood, prod_is_onlineonly, prod_is_set,
                      prod_is_limitedtime, prod_is_pricedown, prod_can_modify, prod_limited_price_date, prod_get_time
                      , table_name, user_name, password)
    except Exception:
        raise
