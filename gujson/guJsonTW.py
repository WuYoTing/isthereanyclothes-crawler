import requests
from bs4 import BeautifulSoup
from gujson.guJsonProdList import getProdList
import time

time_start = time.time();
res = requests.get('https://www.gu-global.com/tw/store')
BS = BeautifulSoup(res.text, "lxml")
for category in BS.select('#globalHeader #navWomen dd .sub2 li a'):
    category_url = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/women' in category_url:
        print(category.text)
        getProdList(category_url)
for category in BS.select('#globalHeader #navMen dd .sub2 li a'):
    category_url = category['href']
    if 'www.gu-global.com/tw/store/feature/gu/men' in category_url:
        print(category.text)
        getProdList(category_url)
time_end = time.time();
print('執行時間: ' + str(round(time_end-time_start, 5)) + ' 秒')
