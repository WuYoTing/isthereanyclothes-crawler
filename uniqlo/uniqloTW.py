import requests
import random
import sys
from bs4 import BeautifulSoup

sys.path.append("..")
from userAgent import USER_AGENT_LIST

USER_AGENT = random.choice(USER_AGENT_LIST)
headers = {'user-agent': USER_AGENT, "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get('https://www.uniqlo.com/tw/', headers=headers)
BS = BeautifulSoup(res.text, "lxml")
for category in BS.select('#navHeader #gnav_wrapper #gnav_main #navHeader a'):
    category_url = category['href']
    print(category_url)

