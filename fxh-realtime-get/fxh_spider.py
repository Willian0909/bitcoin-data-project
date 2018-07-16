# -*- encoding:utf-8 -*-
import requests
from lxml import etree
import time
from selenium import webdriver

class FxhOtc(object):
    def __init__(self):
        self.data = 0
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
        FT = 'https://www.feixiaohao.com/currencies/fcointoken/'
        url_list = [BNB, HT, OKB, BIX, ZB, KCS, BIG, BUT, OTB,FT]

        B_list = []
        for url in url_list:

            S_list = []
            while True:
                try:
                    response = requests.get(url, timeout=30)
                except:
                    time.sleep(1)
                else:
                    html = response.text
                    xml = etree.HTML(html)
                    try:
                        price = xml.xpath("//div[@class='cell maket']/div[4]/span[1]/text()")[0].replace("≈$", "")
                        currency_val = xml.xpath("//div[@class='firstPart']/div[2]/div[3]/text()")[0].replace("≈$",
                                                                                                              "").replace(
                            ",",
                            "").replace(
                            "≈", "")
                        currency_amt = xml.xpath("//div[@class='firstPart']/div[3]/div[2]/text()")[0].replace(' BNB',
                                                                                                              '').replace(
                            ' HT', '').replace(' OKB', '').replace(' BIX', '').replace(' ZB', '').replace(' KCS',
                                                                                                          '').replace(
                            ' BIG', '').replace(' BUT', '').replace(' OTB', '').replace(' FT', '').replace(',',
                                                                                                           '').replace(
                            "≈$", "")
                    except:
                        time.sleep(1)
                    else:

                        if price == '？':
                            price = float(-1)
                        else:
                            price = float(price)

                        if currency_val == '?':
                            currency_value = float(-1)
                        else:
                            currency_value = float(currency_val)

                        if currency_amt == '?':
                            currency_amount = float(-1)
                        else:
                            currency_amount = float(currency_amt)
                        S_list.append(price)
                        S_list.append(currency_value)
                        S_list.append(currency_amount)
                        B_list.append(S_list)
                        break

        return B_list

    def fcoin(self):

        try:
            driver = webdriver.PhantomJS()
            driver.set_page_load_timeout(30)
            driver.get('https://www.fcoin.com/')
            print('数据请求中···')
            ft_secondary = driver.find_element_by_id('ft_secondary').text
            driver.close()
            print("请求的数据为:" + ft_secondary)
            if ft_secondary != '' and ft_secondary != '0':
                result = float(ft_secondary)
                self.data = result
                return result
            else:
                return self.data
        except:
            return self.data

def coindata_get():
    obj = FxhOtc()
    while True:
        ft_secondary = obj.fcoin()
        data_list = obj.fxh()
        data_list[9][2]=ft_secondary
        with open('fxh_file.txt', 'a') as f:
            f.write((time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(time.time()))+':'+str(data_list) + '\n'))
coindata_get()
