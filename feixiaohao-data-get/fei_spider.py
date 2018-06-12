# -*- encoding:utf-8 -*-
import requests
from lxml import etree
import time
import json
class FxhOtc(object):

    def fxh(self):
        BNB = 'https://www.feixiaohao.com/currencies/binance-coin/'
        HT = 'https://www.feixiaohao.com/currencies/ht/'
        OKB = 'https://www.feixiaohao.com/currencies/okb/'
        BIX = 'https://www.feixiaohao.com/currencies/bixtoken/'
        ZB = 'https://www.feixiaohao.com/currencies/zb/'
        KCS = 'https://www.feixiaohao.com/currencies/kcs/'
        BIG = 'https://www.feixiaohao.com/currencies/big/'
        BUT = 'https://www.feixiaohao.com/currencies/bitup/'
        OTB = 'https://www.feixiaohao.com/currencies/otb/'
        url_list = [BNB, HT, OKB, BIX, ZB, KCS, BIG, BUT, OTB]
        B_list = []

        for url in url_list:
            S_list = []
            try:
                response = requests.get(url, timeout=300)
            except:
                continue
            else:
                html = response.text
                xml = etree.HTML(html)
                price = xml.xpath("//div[@class='cell maket']/div[4]/span[1]/text()")[0].replace("≈$", "")
                if price == '？':
                    price = float(-1)
                else:
                    price = float(price)

                currency_val = xml.xpath("//div[@class='firstPart']/div[2]/div[3]/text()")[0].replace("≈$", "").replace(",",
                                                                                                                        "").replace(
                    "≈", "")

                if currency_val == '?':
                    currency_value = float(-1)
                else:
                    currency_value = float(currency_val)
                currency_amt = xml.xpath("//div[@class='firstPart']/div[3]/div[2]/text()")[0].replace(' BNB', '').replace(
                    ' HT', '').replace(' OKB', '').replace(' BIX', '').replace(' ZB', '').replace(' KCS', '').replace(
                    ' BIG', '').replace(' BUT', '').replace(' OTB', '').replace(',', '').replace("≈$", "")
                if currency_amt == '?':
                    currency_amount = float(-1)
                else:
                    currency_amount = float(currency_amt)
                S_list.append(price)
                S_list.append(currency_value)
                S_list.append(currency_amount)
                B_list.append(S_list)

        return B_list

    def otcbtc(self):
        timestamp = ("%.f" % time.time())

        url = 'https://bb.otcbtc.com/exchange/charts/history?symbol=OTBUSDT&resolution=15&from={}&to={}'.format(
            int(timestamp), int(timestamp)+9000)
        response = requests.get(url, timeout=300)
        html = response.text
        ret = json.loads(html)
        new_price = (ret['c'][0])

        return new_price

def coindata_get():
    obj = FxhOtc()
    data_list = obj.fxh()
    while True:
        time.sleep(2)
        with open('feixiaohao.txt', 'a') as f:
            f.write((time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(int("%.f"%time.time())))+':'+str(data_list) + '\n'))
        # otb = obj.otcbtc()
        # with open('fxn.txt', 'a') as f:
        #     f.write((time.strftime("OTB new price:"+str(otb) + '\n')))
        # print("{}最新价为:{}".format((time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(int("%.f"%time.time())))),otb))
coindata_get()