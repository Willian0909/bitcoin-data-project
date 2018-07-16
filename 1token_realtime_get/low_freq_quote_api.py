# -*- coding:utf-8 -*-
import json
from websocket import create_connection
from Api_modules.data_save import data_write
import time

#24小时涨跌幅数据接口
def low_freq_quote(exchange_list):
    while True:
        try:
            ws = create_connection("wss://1token.trade/api/v1/ws/low-freq-quote-v2")
            auth_data = {"uri": "batch-subscribe"}
            ws.send(json.dumps(auth_data))
            for cur in exchange_list:
                cur_list = []
                cur_list.append(cur)
                request_data = {"uri": "batch-subscribe",
                                "contracts": cur_list}
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
                    if "no contract field" in data or "success" in data or 'lost heart beat in 30s'in data:
                        pass
                    else:
                        json_data = json.loads(data)
                        try:
                            currency = json_data['data'][0]['contract']
                        except:
                            break
                        else:
                            if len(json_data['data'])>1:
                                pass
                            else:
                                print(json_data)
                                path = currency.split('/')[0]
                                file_name = currency.replace('/', '_')
                                gategory = "/low_freq_quote/"
                                data_write(path, file_name, data, gategory)
