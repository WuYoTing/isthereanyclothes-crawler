import requests
from bs4 import BeautifulSoup
from lxml import etree


def getPordList(category_url):
    res = requests.get(category_url)
    BS = BeautifulSoup(res.text, "lxml")
    for category in BS.select('#blkMainItemList .thumb a'):
        prod_url = category['href']
        if 'https://www.gu-global.com/tw/store/goods/' in prod_url:
            print(prod_url)
