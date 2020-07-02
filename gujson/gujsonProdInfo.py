import requests


def getProdInfo(prod_num):
    res = requests.get('https://www.gu-global.com/tw/store/ApiGetProductInfo.do?format=json&product=' + prod_num)
    resJson = res.json()
    print(resJson['GoodsInfo']['goods']['goodsNm'])
