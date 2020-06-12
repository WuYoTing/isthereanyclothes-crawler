import requests
from bs4 import BeautifulSoup
from lxml import etree

res = requests.get('https://www.gu-global.com/tw/store/feature/gu/men/longsleevetshirts/')
BS = BeautifulSoup(res.text, "lxml")
for category in BS.select('#globalHeader #navWomen dd .sub2 li a'):
    herf = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/women' in herf:
        print(category.text)
        print(herf)
for category in BS.select('#globalHeader #navMen dd .sub2 li a'):
    herf = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/men' in herf:
        print(category.text)
        print(herf)
