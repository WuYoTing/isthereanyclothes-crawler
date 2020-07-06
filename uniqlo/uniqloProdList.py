import sys

sys.path.append("..")
from getSeleniumPage import getSeleniumPage


def getProdList(prod_list_url):
    prod_url_set = set()
    try:
        page = getSeleniumPage(prod_list_url)
    except Exception as ec:
        raise
    for category in page.select('#airism section dl dd a'):
        prod_url = category['href']
        if 'https://www.uniqlo.com/tw/store/goods' in prod_url:
            prod_url_set.add(prod_url)
    return prod_url_set
