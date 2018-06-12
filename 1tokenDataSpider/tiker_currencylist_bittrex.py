# -*- coding:utf-8 -*-
exchange= 'bittrex'

base_currency1= 'usdt'
trade_currency1= ['btc', 'eth', 'xrp', 'bcc', 'ltc', 'ada', 'trx', 'neo', 'xmr', 'dash', 'etc', 'zec', 'omg', 'btg', 'xvg', 'sc', 'nxt']
base_currency2= 'btc'
trade_currency2= ['eth', 'xrp', 'bcc', 'ltc', 'ada', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'xem', 'etc', 'qtum', 'zec', 'omg', 'lsk', 'btg', 'dcr', 'xvg', 'steem', 'zrx', 'sc', 'waves', 'strat', 'rep', 'doge', 'gnt', 'dgb', 'snt', 'lrc', 'bat', 'kmd', 'ark', 'ardr', 'pivx', 'poly', 'bnt', 'sys', 'rdd', 'mona', 'storm', 'fct', 'xzc', 'eng', 'nxt', 'salt']
base_currency3= 'eth'
trade_currency3= ['xrp', 'bcc', 'ltc', 'ada', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'xem', 'etc', 'qtum', 'zec', 'omg', 'btg', 'zrx', 'sc', 'waves', 'strat', 'rep', 'gnt', 'dgb', 'snt', 'lrc', 'bat', 'poly', 'bnt', 'storm', 'fct', 'eng', 'salt']
def exchange_content():
    #拼接交易所和交易对字符串，例如：bigone/zec.btc
    currency_list_bittrex = []
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
    currency_list_bittrex.extend(currency_list1)
    currency_list_bittrex.extend(currency_list2)
    currency_list_bittrex.extend(currency_list3)

    return currency_list_bittrex


