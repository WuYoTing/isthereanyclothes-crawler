import requests
import random
import traceback
import sys
from bs4 import BeautifulSoup
from exceptionFormat import exceptionFormat
from uniqlo.uniqloProdList import getProdList
import time
import timeit

sys.path.append("..")
from userAgent import USER_AGENT_LIST

totalProdAmout = 0
totalProdListAmout = 0
prod_url_list_set = set()
prod_url_set = set()
tmp_prod_url_set = set()
USER_AGENT = random.choice(USER_AGENT_LIST)
headers = {'user-agent': USER_AGENT, "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get('https://www.uniqlo.com/tw/', headers=headers)
BS = BeautifulSoup(res.text, "lxml")
for category in BS.select('#navHeader .gnav_list .gnav_category #gnav_women li a'):
    category_url = category['href']
    if 'https://www.uniqlo.com/tw/store/feature/women' in category_url:
        if 'https://www.uniqlo.com/tw/store/feature/women/featured' not in category_url and \
                'https://www.uniqlo.com/tw/store/feature/women/special-size' not in category_url:
            print(category.text + ' :' + category_url)
            prod_url_list_set.add(category_url)
for category in BS.select('#navHeader .gnav_list .gnav_category #gnav_men li a'):
    category_url = category['href']
    if 'https://www.uniqlo.com/tw/store/feature/men' in category_url:
        if 'https://www.uniqlo.com/tw/store/feature/men/featured' not in category_url and \
                'https://www.uniqlo.com/tw/store/feature/men/special-size' not in category_url:
            print(category.text + ' :' + category_url)
            prod_url_list_set.add(category_url)

start_time = time.time()
for prod_list_url in prod_url_list_set.copy():
    try:
        tmp_prod_url_set = getProdList(prod_list_url)
    except Exception as ec:
        print("Exception has been thrown. " + str(ec) + "when deal with " + prod_list_url)
        exceptionFormat(ec, prod_list_url)
    else:
        totalProdListAmout = totalProdListAmout + 1
        prod_url_set = prod_url_set.union(tmp_prod_url_set)
        prod_url_list_set.remove(prod_list_url)
end_time = time.time()
for prod_url in prod_url_set:
    totalProdAmout = totalProdAmout + 1
    print(prod_url)
print('uniqlo 共' + str(totalProdListAmout) + ' 個類別 ' + str(totalProdAmout) + '筆產品')
prod_info_total = round(end_time - start_time, 2)
m, s = divmod(prod_info_total, 60)
h, m = divmod(m, 60)
prod_info_total = "%02d:%02d:%02d" % (h, m, s)
print('爬取' + str(totalProdListAmout) + '個類別資訊花了', prod_info_total)
prod_info_total = round(end_time - start_time, 2) / totalProdListAmout
print('平均時間: ' + str(prod_info_total) + '秒')

