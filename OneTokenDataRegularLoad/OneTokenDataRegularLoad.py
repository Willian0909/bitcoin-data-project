# -*- coding: utf-8 -*-
import json
import requests
import time
import re
import sys
import os
class OneTokenEveryday(object):

    def __init__(self):
        # 初始化属性
        self.exchange = 'binance'
        self.dir_name = os.mkdir(self.exchange)
        self.base_currency1 = 'usdt'
        self.trade_currency1 = ['btc', 'eth', 'bcc', 'ltc', 'neo', 'bnb', 'qtum']
        self.base_currency2 = 'btc'
        self.trade_currency2 = ['eth', 'xrp', 'bcc', 'eos', 'ltc', 'ada', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'ven', 'etc',
                           'bnb', 'qtum', 'icx', 'zec', 'omg', 'lsk', 'zil', 'btg', 'ae', 'ont', 'xvg', 'steem', 'zrx',
                           'nano', 'bts', 'ppt', 'bcd', 'waves', 'strat', 'iost', 'snt', 'wtc', 'hsr', 'dgd', 'aion',
                           'lrc', 'bat', 'kmd', 'elf', 'ark', 'pivx', 'bnt', 'gas', 'knc', 'fun', 'gxs', 'cmt', 'sub',
                           'storm', 'xzc', 'eng', 'nuls', 'salt', 'gto']
        self.base_currency3 = 'eth'
        self.trade_currency3 = ['xrp', 'bcc', 'eos', 'ltc', 'ada', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'ven', 'etc', 'bnb',
                           'qtum', 'icx', 'zec', 'omg', 'lsk', 'zil', 'btg', 'ae', 'ont', 'xvg', 'steem', 'zrx', 'nano',
                           'bts', 'ppt', 'bcd', 'waves', 'strat', 'iost', 'snt', 'wtc', 'hsr', 'dgd', 'aion', 'lrc',
                           'bat', 'kmd', 'elf', 'ark', 'pivx', 'bnt', 'knc', 'fun', 'gxs', 'cmt', 'sub', 'storm', 'xzc',
                           'eng', 'nuls', 'salt', 'gto']
        # 定义url模型
        self.count = 0
        self.tiker_url = 'http://alihz-net-0.qbtrade.org/contracts?date={}&format=json'
        self.depth_url = 'http://alihz-net-0.qbtrade.org/hist-ticks?date={}&contract={}&format=json'

    def exchange_content(self):
        # 拼接交易所和交易对字符串，例如：bigone/zec.btc
        currency_binance_list = []
        currency_list1 = []
        for trade in self.trade_currency1:
            currency_name = self.exchange + '/' + trade + '.' + self.base_currency1
            currency_list1.append(currency_name)

        currency_list2 = []
        for trade in self.trade_currency2:
            currency_name = self.exchange + '/' + trade + '.' + self.base_currency2
            currency_list2.append(currency_name)

        currency_list3 = []
        for trade in self.trade_currency3:
            currency_name = self.exchange + '/' + trade + '.' + self.base_currency3
            currency_list3.append(currency_name)
        currency_binance_list.extend(currency_list1)
        currency_binance_list.extend(currency_list2)
        currency_binance_list.extend(currency_list3)
        return currency_binance_list

    def parse(self, url):
        # 发送请求，获取响应数据
        for i in range(999):
            try:
                result = requests.get(url,timeout=300)
                json_str = result.content
            except:
                time.sleep(1)
            else:

                return json_str


    def depth_url_handle(self, file,date, currency):
        #格式化下载页ｕｒｌ
        depth_url = self.depth_url.format(date, currency)
        return depth_url

        # print('获取完毕')

    def data_load(self,url):
        #下载历史数据压缩包
        for i in range(99999):
            time.sleep(2)
            try:
                response = requests.get(url, timeout=300)
                ret = response.content
            except:

                time.sleep(1)
            else:

                u_date = re.findall(r'date=(.*)&', url)[0].replace('&', '').replace('contract=', '-').replace('/', '-')
                # print('正在获取'+u_date+'的数据')
                file_name = './'+self.exchange + '/' + u_date + '.gz'
                size= sys.getsizeof(ret)
                print("压缩包大小："+str("%.3f"%(size/1024))+'kb')
                if size/1024>1:
                    with open(file_name, 'wb') as f:
                        f.write(ret)
                        break
                else:
                    print('下载失败,重新请求')

    def run(self):
        # 获取列表的url可迭代对象
        import time
        datetime = time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400))

        url = self.tiker_url.format(datetime)

        # 获取迭代对象里的url
        for i in range(1000):

            try:
                json_str = self.parse(url)
                # 将返回的数据转换为字典类型的字符串
                ret = json.loads(json_str.decode())
            except:
                print('页面解析失败')

            else:
                file_name = self.exchange + '.txt'
                currency_list = self.exchange_content()

                for currency in currency_list:
                    # 判断查询的数据是否在返回的响应数据中
                    if currency in ret:
                        self.count += 1
                        depth_url = self.depth_url_handle(file_name,datetime, currency)
                        print('正在获取[{}] {}的历史记录！'.format(datetime,currency))
                        self.data_load(depth_url)
                    else:
                        with open('./'+self.exchange + '/'+file_name , 'a') as f:
                            f.write("?" + datetime + '-' + currency + '\n', )
                print(self.count)
                break


if __name__ == '__main__':

    spider = OneTokenEveryday()
    while True:
        spider.run()
        time.sleep(86400)


