from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
from selenium.webdriver.chrome.options import Options
import datetime

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
#
now = datetime.datetime.now()
chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument(f'user-agent={user_agent}')

prod_url = 'https://www.gu-global.com/tw/store/goods/323179'
driverPath = "D:\Python-workspace\SeleniumChromedriver\chromedriver.exe"
driver = webdriver.Chrome(driverPath, options=chrome_options)  # Chrome
driver.get(prod_url)
page_html = driver.page_source
driver.close()

page = BeautifulSoup(page_html, 'lxml')
prod_sex_category = page.select('#content #prodInfo .pathdetail')[0].text
prod_sex = prod_sex_category.split(' ⁄ ')[0].strip()
prod_category = prod_sex_category.split(' ⁄ ')[1].strip()
prod_name = page.select('#content #prodInfo #goodsNmArea')[0].text
prod_price = page.select('#content #prodInfo #basic #price')[0].text.replace('NT$', '')
prod_number = page.select('#content #prodInfo #basic .number')[0].text.replace('商品編號', '')
prod_about = page.select('#content #secondary #prodDetail .content .about')[0].text
prod_material = page.select('#content #secondary #prodDetail .content .about')[0].text
prod_material = page.select('#content #secondary #prodDetail .content .spec dd')[0].text
prod_main_image_url = page.select('#content #secondary #prodMainImg #prodImgDefault')[0].img['src'].replace('model', '')
isnewGood = page.select('#content #prodInfo #goodsIconList #newGood')[0]
isonlineOnlyIcon = page.select('#content #prodInfo #goodsIconList #onlineOnlyIcon')[0]
isSet = page.select('#content #prodInfo #goodsIconList #Set')[0]
islimitedTime = page.select('#content #prodInfo #goodsIconList #limitedTime')[0]
prod_size_url = page.select('#content #prodSelectAttribute #prodSelectSize #selectSizeDetail .linkMore a')[0].get(
    'href')
prod_size_url = prod_size_url.replace("javascript:void(window.open('", "")
prod_size_url = prod_size_url.replace(
    "', '', 'width=600, height=700, status=no, toolbar=no, menubar=no, location=no, resizable=yes, scrollbars=yes'));",
    "")

prod_isnewGood = page.findAll("li", {"id": "newGood"})[0].get('style')
prod_isonlineOnly = page.findAll("li", {"id": "onlineOnlyIcon"})[0].get('style')
prod_isSet = page.findAll("li", {"id": "Set"})[0].get('style')
prod_islimitedTime = page.findAll("li", {"id": "limitedTime"})[0].get('style')
prod_ispriceDown = page.findAll("li", {"id": "priceDown"})[0].get('style')
prod_ismodifyShow = page.findAll("li", {"id": "modifyShow"})[0].get('style')
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
    prod_llimitedPriceDate = str(now.year) + '-' + prod_limitedPriceMonthDay
if prod_ispriceDown == "display: none;":
    prod_ispriceDown = 0
else:
    prod_ispriceDown = 1
if prod_ismodifyShow == "display: none;":
    prod_ismodifyShow = 0
else:
    prod_ismodifyShow = 1

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
print(prod_ismodifyShow)
print(prod_llimitedPriceDate)
