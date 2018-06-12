# -*- coding:utf-8 -*-
exchange= 'huobip'
base_currency1= 'usdt'
trade_currency1= ['btc', 'eth', 'xrp', 'bch', 'eos', 'ltc', 'trx', 'neo', 'dash', 'xem', 'ven', 'etc', 'qtum', 'zec', 'omg', 'zil', 'gnt', 'iost', 'snt', 'hsr', 'nas', 'elf', 'ela', 'ht']
base_currency2= 'btc'
trade_currency2= ['eth', 'xrp', 'bch', 'eos', 'ltc', 'trx', 'neo', 'dash', 'xem', 'ven', 'etc', 'qtum', 'icx', 'zec', 'omg', 'lsk', 'zil', 'btg', 'ont', 'zrx', 'btm', 'bcd', 'gnt', 'iost', 'snt', 'hsr', 'dgd', 'bat', 'nas', 'elf', 'wicc', 'ela', 'gas', 'knc', 'cmt', 'qash', 'ht', 'eng', 'salt']
base_currency3= 'eth'
trade_currency3= ['eos', 'trx', 'ven', 'qtum', 'icx', 'omg', 'lsk', 'zil', 'ont', 'btm', 'gnt', 'iost', 'hsr', 'dgd', 'bat', 'nas', 'elf', 'wicc', 'ela', 'gas', 'cmt', 'qash', 'ht', 'eng', 'salt']

def exchange_content():
    #拼接交易所和交易对字符串，例如：bigone/zec.btc
    currency_list_huobip = []
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
    currency_list_huobip.extend(currency_list1)
    currency_list_huobip.extend(currency_list2)
    currency_list_huobip.extend(currency_list3)

    return currency_list_huobip

