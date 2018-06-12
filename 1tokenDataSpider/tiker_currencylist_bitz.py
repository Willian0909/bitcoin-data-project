# -*- coding:utf-8 -*-
exchange= 'bitz'

base_currency1= 'btc'
trade_currency1= ['eth', 'bch', 'eos', 'ltc', 'trx', 'dash', 'etc', 'qtum', 'zec', 'omg', 'lsk', 'btg', 'bcd', 'doge', 'dgb', 'hsr', 'ark', 'gxs', 'fct', 'nuls']
base_currency2= 'eth'
trade_currency2= ['trx', 'doge', 'gxs', 'nuls']
def exchange_content():
    #拼接交易所和交易对字符串，例如：bigone/zec.btc
    currency_list_binance = []
    currency_list1 = []
    for trade in trade_currency1:
        currency_name = exchange + '/' + trade + '.' + base_currency1
        currency_list1.append(currency_name)

    currency_list2 = []
    for trade in trade_currency2:
        currency_name = exchange + '/' + trade + '.' + base_currency2
        currency_list2.append(currency_name)


    currency_list_binance.extend(currency_list1)
    currency_list_binance.extend(currency_list2)

    return currency_list_binance
