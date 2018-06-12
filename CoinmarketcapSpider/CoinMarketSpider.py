# -*- coding: utf-8 -*-
import time
from lxml import etree
import requests
import re
from selenium import webdriver

class Cion_spider(object):
    def __init__(self):

        self.start_url = 'https://coinmarketcap.com/historical/'
        self.yeary = 0
        self.months = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
                       "July": "07", "August": "08", "September": "09", "October": "10", "November": "11",
                       "December": "12"}
        self.month = 0
        self.day = 0
        #创建浏览器对象1
        self.driver = webdriver.Chrome()
        # 创建浏览器对象2
        self.driver1 = webdriver.Chrome()

    def url_list_handle(self):
        #获取ｙｅａｒ-ｌｉｓｔ
        div_list = self.driver.find_elements_by_xpath("//div[@class='col-lg-10']//div[@class='row']")
        #获取２０１７－２０１8 ｙｅａｒ-ｌｉｓｔ
        want_div = div_list[4:6]
        for div in want_div:
            self.year = div.find_element_by_xpath("./h2").text
            #获取ｍｏｎｔｈ－ｌｉｓｔ
            li_list = div.find_elements_by_xpath("./div[@class='col-sm-4 col-xs-6']")

            for li in li_list:
                month = li.find_element_by_xpath("./h3").text
                self.month = self.months[month]
                print(self.month)
                mouth_li = li.find_elements_by_xpath("./ul//li")
                for m_li in mouth_li:
                    self.day = m_li.find_element_by_xpath("./a").text
                    print(self.day)
                    url = m_li.find_element_by_xpath("./a").get_attribute('href')
                    yield url

    def run(self):
        # 请求起始页数据
        self.driver.get(self.start_url)
        # 根据起始页数据匹配出列表页的url
        url_temp = self.url_list_handle()

        for url in url_temp:
            date_file = self.year + '-' + self.month + '-' + self.day
            print(date_file)

            self.driver1.get(url)
            t_index = self.driver1.find_element_by_xpath("//th[@class='text-center sortable sorting_asc']").text
            t_name = self.driver1.find_element_by_xpath("//th[@id='th-name']").text
            t_symbol = self.driver1.find_element_by_xpath("//th[@id='th-symbol']").text
            t_marketcap = self.driver1.find_element_by_xpath("//th[@id='th-marketcap']").text.replace(" ", '-')
            t_price = self.driver1.find_element_by_xpath("//th[@id='th-price']").text
            t_circulating = self.driver1.find_element_by_xpath("//th[@id='th-totalsupply']").text.replace(" ", '-')
            t_volume = self.driver1.find_element_by_xpath("//th[@id='th-volume']").text.replace(' ', '-')
            t_time = self.driver1.find_element_by_xpath("//th[@id='th-change1h']").text.replace('% ', '')
            t_day = self.driver1.find_element_by_xpath("//th[@id='th-change24h']").text.replace('% ', '')
            t_seven = self.driver1.find_element_by_xpath("//th[@id='th-change7d']").text.replace('% ', '')
            date_file = self.year + '-' + self.month + '-' + self.day
            list_data = t_index + ' ' + t_name + ' ' + t_symbol + ' ' + t_marketcap + ' ' + t_price + ' ' + t_circulating + ' ' + t_volume + ' ' + t_time + ' ' + t_day + ' ' + t_seven

            with open(date_file + '.txt', 'a') as f:
                f.write(list_data + '\n')

            tr_list = self.driver1.find_elements_by_xpath("//tbody//tr")
            for tr in tr_list:

                index = tr.find_element_by_xpath("./td[@class='text-center sorting_1']").text.replace('\n','').replace(' ', '')
                name = tr.find_element_by_xpath("./td[@class='no-wrap currency-name']/a").text.replace('\n','').replace(" ", '-')
                symbol = tr.find_element_by_xpath("./td[@class='text-left col-symbol']").text.replace('$','').replace(',', '').replace('\n', '')
                marketcap = tr.find_element_by_xpath("./td[@class='no-wrap market-cap text-right']").text.replace('$', '').replace(',', '').replace('\n', '').replace(' ', '')
                price = tr.find_element_by_xpath("./td[@class='no-wrap text-right']/a").text.replace('$','').replace(' ', '').strip(' ')
                circulating_suply = tr.find_element_by_xpath( "./td[@class='no-wrap text-right circulating-supply']").text.replace('*', '').replace(',','').replace('$', '').replace('\n', '')
                volume = tr.find_element_by_xpath("./td[@class='no-wrap text-right ']/a").text.replace('$','').replace( ',', '').replace('\n', '')
                time = tr.find_element_by_xpath("./td[8]").text.replace('%', '').replace(' ', '')
                day = tr.find_element_by_xpath("./td[9]").text.replace('%', '').replace(' ', '')
                seven = tr.find_element_by_xpath("./td[10]").text.replace('%', '').replace(' ', '')
                list_data = index + ' ' + name + ' ' + symbol + ' ' + marketcap + ' ' + price + ' ' + circulating_suply  + volume + ' ' + time + ' ' + day + ' ' + seven

                with open(date_file + '.txt', 'a') as f:
                    f.write(list_data + '\n')

if __name__ == '__main__':
    coin = Cion_spider()
    coin.run()
