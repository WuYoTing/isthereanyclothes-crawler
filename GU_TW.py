import requests
from bs4 import BeautifulSoup
from lxml import etree
from GU_List import getPordList

res = requests.get('https://www.gu-global.com/tw/store')
BS = BeautifulSoup(res.text, "lxml")
for category in BS.select('#globalHeader #navWomen dd .sub2 li a'):
    category_url = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/women' in category_url:
        print(category.text)
        getPordList(category_url)
for category in BS.select('#globalHeader #navMen dd .sub2 li a'):
    category_url = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/men' in category_url:
        print(category.text)
        getPordList(category_url)
