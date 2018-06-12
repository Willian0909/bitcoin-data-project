# -*- encoding:utf-8 -*-

import json

def currency_data():

    file_list = ['precise-binance.txt','precise-huobi.txt','precise-okex.txt']

    for file_name in file_list:

        if file_name =='precise-binance.txt':

            with open(file_name, 'r') as f:
                data_str = f.readlines()

                for data in data_str:
                    dt = data.replace('\n', '')
                    dt_list = dt.split(',')


                    if dt_list[0].endswith('btc'):

                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_btc'
                            if dt_list[0]==currency:
                                a = dt_list[3]


                                json_str = {coin+'btc': {"price_precision": int(dt_list[1]), "amount_precision": int(dt_list[2]),
                                                    "min_amount": dt_list[3], "max_amount": dt_list[4]}}
                                with open('./currency_data/precise-binance_btc.json','a') as f:
                                    f.write(json.dumps(json_str)+'\n')
                            else:
                                continue

                    elif dt_list[0].endswith('eth'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_eth'
                            if dt_list[0] == currency:
                                json_str = {coin+'eth': {"price_precision": int(dt_list[1]), "amount_precision": int(dt_list[2]),
                                                    "min_amount": dt_list[3], "max_amount": dt_list[4]}}
                                with open('./currency_data/precise-binance_eth.json','a') as f:
                                    f.write(json.dumps(json_str)+'\n')

                    elif dt_list[0].endswith('usdt'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_usdt'
                            if dt_list[0] == currency:
                                json_str = {coin+'usdt': {"price_precision": int(dt_list[1]), "amount_precision": int(dt_list[2]),
                                                    "min_amount": dt_list[3], "max_amount": dt_list[4]}}
                                with open('./currency_data/precise-binance_usdt.json','a') as f:
                                    f.write(json.dumps(json_str)+'\n')
                    else:
                        continue
        elif file_name =='precise-huobi.txt':
            with open(file_name, 'r') as f:
                data_str = f.readlines()

                for data in data_str:
                    dt = data.replace('\n', '')
                    dt_list = dt.split(',')

                    if dt_list[0].endswith('btc'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_btc'
                            if dt_list[0] == currency:
                                json_str = {coin+'btc': {"price_precision": int(dt_list[1]),
                                                   "amount_precision": int(dt_list[2])}}
                                with open('./currency_data/precise-huobi_btc.json','a') as f:
                                    f.write(json.dumps(json_str)+'\n')

                    elif dt_list[0].endswith('eth'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_eth'
                            if dt_list[0] == currency:
                                json_str = {coin+'eth':{"price_precision": int(dt_list[1]),
                                                   "amount_precision": int(dt_list[2])}}
                                with open('./currency_data/precise-huobi_eth.json','a') as f:
                                    f.write(json.dumps(json_str)+'\n')

                    elif dt_list[0].endswith('usdt'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_usdt'
                            if dt_list[0] == currency:
                                json_str = {coin + 'usdt': {"price_precision": int(dt_list[1]),
                                                           "amount_precision": int(dt_list[2])}}
                                with open('./currency_data/precise-huobi_usdt.json', 'a') as f:
                                    f.write(json.dumps(json_str) + '\n')
                            else:
                                continue
        else:

            with open(file_name, 'r') as f:
                data_str = f.readlines()

                for data in data_str:
                    dt = data.replace('\n', '')
                    dt_list = dt.split(',')

                    if dt_list[0].endswith('btc'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]

                        for coin in coin_list:
                            currency = coin + '_btc'
                            if dt_list[0] == currency:
                                json_str = {coin+'btc': {"price_precision": int(dt_list[1]), "amount_precision": int(dt_list[2]),
                                                    "min_amount": float(dt_list[3])}}
                                with open('./currency_data/precise-okex_btc.json', 'a') as f:
                                    f.write(json.dumps(json_str)+'\n')

                    elif dt_list[0].endswith('eth'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_eth'
                            if dt_list[0] == currency:
                                json_str = {coin+'eth': {"price_precision": int(dt_list[1]), "amount_precision": int(dt_list[2]),
                                                    "min_amount": float(dt_list[3])}}
                                with open('./currency_data/precise-okex_eth.json', 'a') as f:
                                    f.write(json.dumps(json_str)+'\n')

                    elif dt_list[0].endswith('usdt'):
                        coin_list = ["btc", "eth", "xrp", "bch", "eos", "ltc", "ada", "xlm", "miota", "trx"]
                        for coin in coin_list:
                            currency = coin + '_usdt'
                            if dt_list[0] == currency:
                                json_str = {coin + 'usdt': {"price_precision": int(dt_list[1]),
                                                           "amount_precision": int(dt_list[2]),
                                                           "min_amount": float(dt_list[3])}}
                                with open('./currency_data/precise-okex_usdt.json', 'a') as f:
                                    f.write(json.dumps(json_str) + '\n')
                            else:
                                continue
currency_data()