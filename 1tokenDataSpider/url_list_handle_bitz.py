# -*- coding: utf-8 -*-
import json
import requests

from tiker_currencylist_bitz import exchange_content


class TokenTrade(object):
    def __init__(self):
        # 初始化属性

        self.count = 0
        # 定义url模型
        self.tiker_url = 'http://alihz-net-0.qbtrade.org/contracts?date={}&format=json'
        self.depth_url = 'http://alihz-net-0.qbtrade.org/hist-ticks?date={}&contract={}&format=json'

    def parse(self, url):
        # 发送请求，获取响应数据
        try:
            result = requests.get(url,timeout=300)
            json_str = result.content
        except Exception as e:
            print(e)
            try:
                result = requests.get(url, timeout=300)
                json_str = result.content
            except Exception as e:
                print(e)

            else:
                return json_str
        else:
            return json_str

    def depth_url_handle(self, file,date, currency):
        depth_url = self.depth_url.format(date, currency)

        print(depth_url)
        with open('./download_file/' + file, 'a') as f:
            f.write(depth_url + '\n', )

    def run(self):

        with open('date-list.txt', 'r') as f:
            date_time = f.readlines()[0].replace('[', '').replace(']', '')

            dt_list = date_time.split(',')

            for dt in dt_list:

                date = dt.replace("'", "").replace(' ','')
                print(date)

                url = self.tiker_url.format(date)

                # 获取迭代对象里的url

                json_str = self.parse(url)

                # 将返回的数据转换为字典类型的字符串
                ret = json.loads(json_str.decode())

                print('正在获取[{}]日的历史记录！'.format(date))
                # 拼接历史交易记录保存路径
                file_name = 'bitz' + '.txt'

                currency_list = exchange_content()

                for currency in currency_list:
                    # 判断查询的数据是否在返回的响应数据中
                    if currency in ret:
                        self.count += 1
                        self.depth_url_handle(file_name,date, currency)
                    else:
                        with open('./download_file/' + file_name, 'a') as f:
                            f.write("?" + date + '-' + currency + '\n', )

                print(self.count)

if __name__ == '__main__':

    spider = TokenTrade()
    spider.run()

