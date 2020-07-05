import requests
import random
import traceback
import sys
from bs4 import BeautifulSoup
from exceptionFormat import exceptionFormat
from uniqlo.uniqloProdList import getProdList

sys.path.append("..")
from userAgent import USER_AGENT_LIST

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
        print(category.text + ' :' + category_url)
        prod_url_list_set.add(category_url)
for prod_list_url in prod_url_list_set.copy():
    try:
        tmp_prod_url_set = getProdList(prod_list_url)
    except Exception as ec:
        exceptionFormat(ec,prod_list_url)
    else:
        prod_url_set = prod_url_set.union(tmp_prod_url_set)
        prod_url_list_set.remove(prod_list_url)

for prod_url in prod_url_set:
    print(prod_url)