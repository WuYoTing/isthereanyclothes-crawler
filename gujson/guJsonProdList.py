import requests
from bs4 import BeautifulSoup
from gujson.gujsonProdInfo import getProdInfo


def getProdList(category_url):
    res = requests.get(category_url)
    BS = BeautifulSoup(res.text, "lxml")
    for category in BS.select('#blkMainItemList .thumb a'):
        prod_url = category['href']
        if 'https://www.gu-global.com/tw/store/goods/' in prod_url:
            prod_num = prod_url.replace('https://www.gu-global.com/tw/store/goods/', '')
            getProdList(prod_num)
