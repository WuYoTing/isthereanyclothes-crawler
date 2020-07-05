import requests
import sys
import traceback
import time
from bs4 import BeautifulSoup
from gu.guProdInfo import getProdInfo
from mailLog import maillog
from exceptionFormat import exceptionFormat

prod_url_set = set()
start_time = time.time()
res = requests.get('https://www.gu-global.com/tw/store')
BS = BeautifulSoup(res.text, "lxml")
for category in BS.select('#globalHeader #navWomen dd .sub2 li a'):
    category_url = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/women' in category_url:
        print(category.text)
        category_res = requests.get(category_url)
        BS = BeautifulSoup(category_res.text, "lxml")
        for category in BS.select('#blkMainItemList .thumb a'):
            prod_url = category['href']
            if 'https://www.gu-global.com/tw/store/goods/' in prod_url:
                print(prod_url)
                prod_url_set.add(prod_url)

for category in BS.select('#globalHeader #navMen dd .sub2 li a'):
    category_url = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/men' in category_url:
        print(category.text)
        category_res = requests.get(category_url)
        BS = BeautifulSoup(category_res.text, "lxml")
        for category in BS.select('#blkMainItemList .thumb a'):
            prod_url = category['href']
            if 'https://www.gu-global.com/tw/store/goods/' in prod_url:
                print(prod_url)
                prod_url_set.add(prod_url)

prod_url_end_time = time.time()
print('爬取所有產品網址花了', prod_url_end_time - start_time, 'seconds')
for prod_url in prod_url_set.copy():
    print(prod_url)
    try:
        getProdInfo(prod_url)
    except Exception as ec:
        exceptionFormat(ec, prod_url)
    else:
        prod_url_set.remove(prod_url)
prod_info_end_time = time.time()
prod_info_total = round(prod_info_end_time-prod_url_end_time,2)
m, s = divmod(prod_info_total, 60)
h, m = divmod(m, 60)
prod_info_total = "%02d:%02d:%02d" % (h, m, s)
print('爬取所有產品資訊花了', prod_info_total, 'seconds')
maillog('Crawler Success', 'Crawler_GU done successful in' + str(prod_info_total) + '秒',
        'hakosaki314@gmail.com')
