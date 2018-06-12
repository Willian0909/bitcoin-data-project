# -*- coding:utf-8 -*-
exchange= 'binance'
base_currency1 = 'usdt'
trade_currency1 = ['btc', 'eth', 'bcc', 'ltc', 'neo', 'bnb', 'qtum']
base_currency2 = 'btc'
trade_currency2= ['eth', 'xrp', 'bcc', 'eos', 'ltc', 'ada', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'ven', 'etc', 'bnb', 'qtum', 'icx', 'zec', 'omg', 'lsk', 'zil', 'btg', 'ae', 'ont', 'xvg', 'steem', 'zrx', 'nano', 'bts', 'ppt', 'bcd', 'waves', 'strat', 'iost', 'snt', 'wtc', 'hsr', 'dgd', 'aion', 'lrc', 'bat', 'kmd', 'elf', 'ark', 'pivx', 'bnt', 'gas', 'knc', 'fun', 'gxs', 'cmt', 'sub', 'storm', 'xzc', 'eng', 'nuls', 'salt', 'gto']
base_currency3 = 'eth'
trade_currency3 = ['xrp', 'bcc', 'eos', 'ltc', 'ada', 'xlm', 'trx', 'neo', 'xmr', 'dash', 'ven', 'etc', 'bnb', 'qtum', 'icx', 'zec', 'omg', 'lsk', 'zil', 'btg', 'ae', 'ont', 'xvg', 'steem', 'zrx', 'nano', 'bts', 'ppt', 'bcd', 'waves', 'strat', 'iost', 'snt', 'wtc', 'hsr', 'dgd', 'aion', 'lrc', 'bat', 'kmd', 'elf', 'ark', 'pivx', 'bnt', 'knc', 'fun', 'gxs', 'cmt', 'sub', 'storm', 'xzc', 'eng', 'nuls', 'salt', 'gto']
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

    currency_list3 = []
    for trade in trade_currency3:
        currency_name = exchange + '/' + trade + '.' + base_currency3
        currency_list3.append(currency_name)
    currency_list_binance.extend(currency_list1)
    currency_list_binance.extend(currency_list2)
    currency_list_binance.extend(currency_list3)

    return currency_list_binance
