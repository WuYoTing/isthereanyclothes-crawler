import requests
import random
import math
import sys
from bs4 import BeautifulSoup
from exception.exceptionFormat import exceptionFormat
from crawler.prodInfoGet import getProdInfo

sys.path.append("..")
from user_agent_list.userAgent import USER_AGENT_LIST


def getUniqloProd(driver, userName, password):
    USER_AGENT = random.choice(USER_AGENT_LIST)
    headers = {'user-agent': USER_AGENT, "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
    # 男生
    manProdUrlSet = set()
    res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=001', headers=headers)
    BS = BeautifulSoup(res.text, "lxml")
    manProdAmount = int(BS.select('#content .blkPaginationTop tr th')[0].text.replace('搜尋結果：', '').replace('件', ''))
    manProdPage = math.ceil(manProdAmount / 48)
    for page in range(manProdPage):
        manQstart = page * 48
        res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=001&qstart=' + str(manQstart), headers=headers)
        BS = BeautifulSoup(res.text, "lxml")
        for category in BS.select('#blkMainItemList .unit .info .name a'):
            category_url = category['href']
            if 'https://www.uniqlo.com/tw/store/goods/' in category_url:
                manProdUrlSet.add(category_url)
    # 女生
    womanProdUrlSet = set()
    res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=002', headers=headers)
    BS = BeautifulSoup(res.text, "lxml")
    womanProdAmount = int(BS.select('#content .blkPaginationTop tr th')[0].text.replace('搜尋結果：', '').replace('件', ''))
    womanProdPage = math.ceil(womanProdAmount / 48)
    for page in range(womanProdPage):
        womanQstart = page * 48
        res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=002&qstart=' + str(womanQstart),
                           headers=headers)
        BS = BeautifulSoup(res.text, "lxml")
        for category in BS.select('#blkMainItemList .unit .info .name a'):
            category_url = category['href']
            if 'https://www.uniqlo.com/tw/store/goods/' in category_url:
                womanProdUrlSet.add(category_url)
    for prod_url in manProdUrlSet.copy():
        print(str(len(manProdUrlSet)) + ' items left for man in uniqlo')
        try:
            getProdInfo(prod_url, driver, 'uniqlo_clothes', userName, password)
        except Exception as ec:
            exceptionFormat(ec, prod_url)
        else:
            manProdUrlSet.remove(prod_url)
    for prod_url in womanProdUrlSet.copy():
        print(str(len(womanProdUrlSet)) + ' items left for woman in uniqlo')
        try:
            getProdInfo(prod_url, driver, 'uniqlo_clothes', userName, password)
        except Exception as ec:
            exceptionFormat(ec, prod_url)
        else:
            womanProdUrlSet.remove(prod_url)