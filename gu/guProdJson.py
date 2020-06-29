import requests


def getProdJson(prod_number):
    res = requests.get('https://www.gu-global.com/tw/store/ApiGetProductInfo.do?format=json&product=' + prod_number)
    resJson = res.json()
    print(resJson['GoodsInfo']['goods']['goodsNm'])


getProdJson('32222200001')
