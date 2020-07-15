import requests
import random
import math
import sys
from bs4 import BeautifulSoup
from exceptionFormat import exceptionFormat
from crawlerUniqoGu.prodInfoGet import getProdInfo

sys.path.append("..")
from userAgent import USER_AGENT_LIST


def getGuProd(driver):
    USER_AGENT = random.choice(USER_AGENT_LIST)
    headers = {'user-agent': USER_AGENT, "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
    # 男生
    manProdUrlSet = set()
    res = requests.get('https://www.gu-global.com/tw/store/search?qbrand=20&qclv1=001', headers=headers)
    BS = BeautifulSoup(res.text, "lxml")

    manProdAmount = int(BS.select('#content .blkPaginationTop tr th')[0].text.replace('搜尋結果：', '').replace('件', ''))
    manProdPage = math.ceil(manProdAmount / 48)
    for page in range(manProdPage):
        manQstart = page * 48
        res = requests.get('https://www.gu-global.com/tw/store/search?qbrand=20&qclv1=001&qstart=' + str(manQstart), headers=headers)
        BS = BeautifulSoup(res.text, "lxml")
        for category in BS.select('#blkMainItemList .unit .info .name a'):
            category_url = category['href']
            if 'https://www.gu-global.com/tw/store/goods/' in category_url:
                manProdUrlSet.add(category_url)
    # 女生
    womanProdUrlSet = set()
    res = requests.get('https://www.gu-global.com/tw/store/search?qbrand=20&qclv1=002', headers=headers)
    BS = BeautifulSoup(res.text, "lxml")
    womanProdAmount = int(BS.select('#content .blkPaginationTop tr th')[0].text.replace('搜尋結果：', '').replace('件', ''))
    womanProdPage = math.ceil(womanProdAmount / 48)
    for page in range(womanProdPage):
        womanQstart = page * 48
        res = requests.get('https://www.gu-global.com/tw/store/search?qbrand=20&qclv1=002&qstart=' + str(womanQstart),
                           headers=headers)
        BS = BeautifulSoup(res.text, "lxml")
        for category in BS.select('#blkMainItemList .unit .info .name a'):
            category_url = category['href']
            if 'https://www.gu-global.com/tw/store/goods' in category_url:
                womanProdUrlSet.add(category_url)
    for prod_url in manProdUrlSet.copy():
        try:
            getProdInfo(prod_url, driver,'gu_clothes')
        except Exception as ec:
            exceptionFormat(ec, prod_url)
        else:
            manProdUrlSet.remove(prod_url)
    for prod_url in womanProdUrlSet.copy():
        try:
            getProdInfo(prod_url, driver)
        except Exception as ec:
            exceptionFormat(ec, prod_url)
        else:
            womanProdUrlSet.remove(prod_url)