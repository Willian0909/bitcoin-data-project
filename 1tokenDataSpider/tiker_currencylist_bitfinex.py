# -*- coding:utf-8 -*-

exchange= 'bitfinex'
base_currency1= 'usd'
trade_currency1= ['btc', 'eth', 'xrp', 'bch', 'eos', 'ltc', 'xlm', 'trx', 'neo', 'xmr', 'ven', 'etc', 'zec', 'omg', 'btg', 'xvg', 'zrx', 'rep', 'mkr', 'gnt', 'snt', 'lrc', 'bat', 'elf', 'knc', 'fun']
base_currency2= 'btc'
trade_currency2= ['eth', 'xrp', 'bch', 'eos', 'ltc', 'xlm', 'trx', 'neo', 'xmr', 'ven', 'etc', 'zec', 'omg', 'btg', 'xvg', 'zrx', 'rep', 'mkr', 'gnt', 'snt', 'lrc', 'bat', 'elf', 'knc', 'fun']
base_currency3= 'eth'
trade_currency3= ['bch', 'eos', 'xlm', 'trx', 'neo', 'ven', 'omg', 'xvg', 'zrx', 'rep', 'mkr', 'gnt', 'snt', 'lrc', 'bat', 'elf', 'knc', 'fun']
def exchange_content():
    #拼接交易所和交易对字符串，例如：bigone/zec.btc
    currency_list_bitfinex = []
    currency_list1 = []
    for trade in trade_currency1:
        currency_name = exchange + '/' + trade + '.' + base_currency1
        currency_list1.append(currency_name)

    currency_list2 = []
    for trade in trade_currency2:
        currency_name = exchange + '/' + trade + '.' + base_currency2
        currency_list2.append(currency_name)

    currency_list3 = []
    for trade in trade_currency3:
        currency_name = exchange + '/' + trade + '.' + base_currency3
        currency_list3.append(currency_name)
    currency_list_bitfinex.extend(currency_list1)
    currency_list_bitfinex.extend(currency_list2)
    currency_list_bitfinex.extend(currency_list3)

    return currency_list_bitfinex
