# -*- coding:utf-8 -*-
exchange = 'okex'

base_currency1 = 'usdt'
trade_currency1 = ['btc', 'eth', 'xrp', 'bch', 'eos', 'ltc', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'xem', 'etc', 'qtum', 'icx', 'zec', 'omg', 'btg', 'ont', 'zrx', 'nano', 'btm', 'ppt', 'bcd', 'mkr', 'gnt', 'dgb', 'iost', 'snt', 'wtc', 'hsr', 'dgd', 'lrc', 'nas', 'elf', 'ark', 'bnt', 'gas', 'knc', 'fun', 'mith', 'cmt', 'sub', 'hot', 'eng', 'nuls', 'salt', 'gto']
base_currency2= 'btc'
trade_currency2= ['eth', 'xrp', 'bch', 'eos', 'ltc', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'xem', 'etc', 'qtum', 'icx', 'zec', 'omg', 'btg', 'ont', 'zrx', 'nano', 'btm', 'ppt', 'bcd', 'mkr', 'gnt', 'dgb', 'iost', 'snt', 'wtc', 'hsr', 'dgd', 'lrc', 'nas', 'elf', 'ark', 'bnt', 'gas', 'knc', 'fun', 'mith', 'cmt', 'sub', 'hot', 'eng', 'nuls', 'salt', 'gto']
base_currency3= 'eth'
trade_currency3= ['xrp', 'bch', 'eos', 'ltc', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'xem', 'etc', 'qtum', 'icx', 'zec', 'omg', 'ont', 'zrx', 'nano', 'btm', 'ppt', 'mkr', 'gnt', 'dgb', 'iost', 'snt', 'wtc', 'hsr', 'dgd', 'lrc', 'nas', 'elf', 'ark', 'bnt', 'gas', 'knc', 'fun', 'mith', 'cmt', 'sub', 'hot', 'eng', 'nuls', 'salt', 'gto']
def exchange_content():
    #拼接交易所和交易对字符串，例如：bigone/zec.btc
    currency_list_okex = []
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
    currency_list_okex.extend(currency_list1)
    currency_list_okex.extend(currency_list2)
    currency_list_okex.extend(currency_list3)

    return currency_list_okex
