import requests
import random
import math
import traceback
import sys
from bs4 import BeautifulSoup
from exceptionFormat import exceptionFormat
from uniqlo.uniqloProdList import getProdList
import time
from getSeleniumPage import createDriverInstance

sys.path.append("..")
from userAgent import USER_AGENT_LIST

USER_AGENT = random.choice(USER_AGENT_LIST)
headers = {'user-agent': USER_AGENT, "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}

# 男生
manActual = 0
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
            manActual += 1
# 女生
womanActual = 0
res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=002', headers=headers)
BS = BeautifulSoup(res.text, "lxml")
womanProdAmount = int(BS.select('#content .blkPaginationTop tr th')[0].text.replace('搜尋結果：', '').replace('件', ''))
womanProdPage = math.ceil(womanProdAmount / 48)
for page in range(womanProdPage):
    womanQstart = page * 48
    res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=002&qstart=' + str(womanQstart), headers=headers)
    BS = BeautifulSoup(res.text, "lxml")
    for category in BS.select('#blkMainItemList .unit .info .name a'):
        category_url = category['href']
        if 'https://www.uniqlo.com/tw/store/goods/' in category_url:
            womanActual += 1

print('爬到的男生產品共:' + str(manActual))
print('爬到的女生產品共:' + str(womanActual))
print('男生共:' + str(manProdAmount) + '個產品 ' + str(manProdPage) + '頁')
print('女生共:' + str(womanProdAmount) + '個產品 ' + str(womanProdPage) + '頁')
