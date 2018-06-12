# -*- coding:utf-8 -*-
exchange= 'kraken'
base_currency1= 'usd'
trade_currency1= ['eth', 'xrp', 'bch', 'eos', 'ltc', 'xlm', 'xmr', 'dash', 'usdt', 'etc', 'zec', 'rep']

base_currency2= 'eth'
trade_currency2= ['eos', 'etc', 'rep']
def exchange_content():
    #拼接交易所和交易对字符串，例如：bigone/zec.btc
    currency_list_kraken = []
    currency_list1 = []
    for trade in trade_currency1:
        currency_name = exchange + '/' + trade + '.' + base_currency1
        currency_list1.append(currency_name)

    currency_list2 = []
    for trade in trade_currency2:
        currency_name = exchange + '/' + trade + '.' + base_currency2
        currency_list2.append(currency_name)
    currency_list_kraken.extend(currency_list1)
    currency_list_kraken.extend(currency_list2)


    return currency_list_kraken
