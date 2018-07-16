# -*- coding:utf-8 -*-
import gzip
import io
import json
from websocket import create_connection
from data_save import data_write
import time

#实时tick-v3行情 （Alpha）
def tike_v3_parse(currency_list):
    while True:
        try:
            ws = create_connection("wss://1token.trade/api/v1/ws/tick-v3")
            auth_data = {"uri": "auth"}
            ws.send(json.dumps(auth_data))
            for cur in currency_list:
                request_data = {"uri": "subscribe-single-tick-verbose",
                                "contract": cur}
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
                    fio = io.BytesIO(data)
                    f = gzip.GzipFile(fileobj=fio)
                    data_str = f.read().decode('utf-8')
                    if "lost heart beat in 30s" in data_str or "Auth succeed." in data_str or "doesn't exist" in data_str:
                        pass
                    else:
                        json_str = json.loads(data_str)
                        currency = json_str['c']
                        path = currency.split('/')[0]
                        file_name = currency.replace('/', '_')
                        gategory = "/tike_v3/"
                        data_write(path, file_name, data_str,gategory)
