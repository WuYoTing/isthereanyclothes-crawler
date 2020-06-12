import requests
from bs4 import BeautifulSoup
from lxml import etree

res = requests.get('https://www.gu-global.com/tw/store/feature/gu/men/roomwear/')
BS = BeautifulSoup(res.text, "lxml")
for category in BS.select('#blkMainItemList .thumb a'):
    herf = category['href']
    print(herf)