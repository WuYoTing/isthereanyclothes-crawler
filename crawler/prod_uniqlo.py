import requests
import random
import math
from bs4 import BeautifulSoup
from exception.exception_format import exception_format
from crawler.prod_Info_get import get_prod_info
from user_agent_list.userAgent import user_agent_list


def get_uniqlo_prod(driver, db_host, db_name, db_user_name, db_password, mail_user, mail_password, recipient):
    user_agent = random.choice(user_agent_list)
    headers = {'user-agent': user_agent, "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
    # 取男生所有產品
    man_prod_url_set = set()
    man_index_res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=001', headers=headers)
    man_index_bs = BeautifulSoup(man_index_res.text, "lxml")
    man_prod_amount = int(
        man_index_bs.select('#content .blkPaginationTop tr th')[0].text.replace('搜尋結果：', '').replace('件', ''))
    man_prod_page = math.ceil(man_prod_amount / 48)
    for page in range(man_prod_page):
        man_page_index = page * 48
        man_page_res = requests.get(
            'https://www.uniqlo.com/tw/store/search?qclv1=001&qstart=' + str(man_page_index),
            headers=headers)
        man_page_bs = BeautifulSoup(man_page_res.text, "lxml")
        for category in man_page_bs.select('#blkMainItemList .unit .info .name a'):
            category_url = category['href']
            if 'https://www.uniqlo.com/tw/store/goods/' in category_url:
                man_prod_url_set.add(category_url)
    # 取女生所有產品
    woman_prod_url_set = set()
    woman_index_res = requests.get('https://www.uniqlo.com/tw/store/search?qclv1=002', headers=headers)
    woman_index_bs = BeautifulSoup(woman_index_res.text, "lxml")
    woman_prod_amount = int(
        woman_index_bs.select('#content .blkPaginationTop tr th')[0].text.replace('搜尋結果：', '').replace('件', ''))
    woman_prod_page = math.ceil(woman_prod_amount / 48)
    for page in range(woman_prod_page):
        woman_page_index = page * 48
        woman_page_res = requests.get(
            'https://www.uniqlo.com/tw/store/search?qclv1=002&qstart=' + str(woman_page_index),
            headers=headers)
        woman_page_bs = BeautifulSoup(woman_page_res.text, "lxml")
        for category in woman_page_bs.select('#blkMainItemList .unit .info .name a'):
            category_url = category['href']
            if 'https://www.uniqlo.com/tw/store/goods/' in category_url:
                woman_prod_url_set.add(category_url)
    # 取男生產品內容
    for prod_url in man_prod_url_set.copy():
        print(str(len(man_prod_url_set)) + ' items left for man in uniqlo')
        try:
            get_prod_info(prod_url, driver, 'uniqlo_clothes', db_host, db_name, db_user_name, db_password)
        except Exception as Ec:
            exception_format(mail_user, mail_password, recipient, Ec, prod_url)
        else:
            man_prod_url_set.remove(prod_url)
    # 取女生產品內容
    for prod_url in woman_prod_url_set.copy():
        print(str(len(woman_prod_url_set)) + ' items left for woman in uniqlo')
        try:
            get_prod_info(prod_url, driver, 'uniqlo_clothes', db_host, db_name, db_user_name, db_password)
        except Exception as Ec:
            exception_format(mail_user, mail_password, recipient, Ec, prod_url)
        else:
            woman_prod_url_set.remove(prod_url)
