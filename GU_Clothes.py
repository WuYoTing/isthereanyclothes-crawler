from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree

prod_url = 'https://www.gu-global.com/tw/store/goods/325249'
driverPath = "D:\Python-workspace\SeleniumChromedriver\chromedriver.exe"
driver = webdriver.Chrome(driverPath)  # Chrome
driver.get(prod_url)
page_html = driver.page_source
driver.close()

page = BeautifulSoup(page_html, 'lxml')
prod_sex_category = page.select('#content #prodInfo .pathdetail')[0].text
prod_sex = prod_sex_category.split(' ⁄ ')[0].strip()
prod_category = prod_sex_category.split(' ⁄ ')[1].strip()
prod_name = page.select('#content #prodInfo #goodsNmArea')[0].text
prod_price_text = page.select('#content #prodInfo #basic #price')[0].text
prod_number = page.select('#content #prodInfo #basic .number')[0].text.replace('商品編號', '')
# 缺一塊 新品 特價 網路限定特價 的判斷
prod_comment = page.select('#content #secondary #prodDetail .content .about')[0].text
prod_material = page.select('#content #secondary #prodDetail .content .about')[0].text
prod_material = page.select('#content #secondary #prodDetail .content .spec dd')[0].text
# 抓到錯誤的url
prod_main_image_url = page.select('#content #secondary #prodMainImg #prodImgDefault')[0].img['src'].replace('model', '')
isnewGood = page.select('#content #prodInfo #goodsIconList #newGood')[0]
isonlineOnlyIcon = page.select('#content #prodInfo #goodsIconList #onlineOnlyIcon')[0]
isSet = page.select('#content #prodInfo #goodsIconList #Set')[0]
islimitedTime = page.select('#content #prodInfo #goodsIconList #limitedTime')[0]
sizeUrl = page.select('#content #tertiary #prodSelectAttribute #selectSizeDetail .linkMore .external')[0].get('href')
isnewGood = page.findAll("li", {"id": "newGood"})[0].get('style')
isonlineOnlyIcon = page.findAll("li", {"id": "onlineOnlyIcon"})[0].get('style')
isSet = page.findAll("li", {"id": "Set"})[0].get('style')
islimitedTime = page.findAll("li", {"id": "limitedTime"})[0].get('style')
ispriceDown = page.findAll("li", {"id": "priceDown"})[0].get('style')
ismodifyShow = page.findAll("li", {"id": "modifyShow"})[0].get('style')

print(prod_sex)
print(prod_category)
print(prod_name)
print(prod_price_text)
print(prod_number)
print(prod_comment)
print(prod_material)
print(prod_url)
print(prod_main_image_url)
print(sizeUrl)
print(isnewGood)
print(isonlineOnlyIcon)
print(isSet)
print(islimitedTime)
print(ispriceDown)
print(ismodifyShow)
