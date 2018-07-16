# -*- coding:utf-8 -*-
import json
import time
from websocket import create_connection
from data_save import data_write

def candle_parse(currency_list):
    while True:
        try:
            ws = create_connection("wss://1token.trade/api/v1/ws/candle")
            for cur in currency_list:
                request_data = {
            "contract":cur,
            "duration": "1m"}
                ws.send(json.dumps(request_data))
        except:
            time.sleep(0.5)
        else:
            while True:
                try:
                    data = ws.recv()
                except:
                    break
                else:
                    if "lost heart beat in 30s" in data or "Auth succeed." in data:
                        pass
                    else:
                        # print(data)
                        json_data = json.loads(data)
                        currency = json_data['contract']
                        category = "/kline/"
                        path = currency.split('/')[0]
                        file_name = currency.replace('/','_')

                        data_write(path, file_name, data, category)


