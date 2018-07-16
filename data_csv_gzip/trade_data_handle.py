#-*- encoding:utf-8 -*-
import csv
import zipfile
import json
import time

#写入csv文件
def csv_write(list,file_name):
       with open(file_name,"a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['exchange','trade_currency','base_currency','price','amount','direction','order_id','order_ts','id','ts','butts','exchange_ts'])
        writer.writerows(list)
#压缩文件
def zip_files(zip_name ):
    zip = zipfile.ZipFile( zip_name+".gz", 'w', zipfile.ZIP_DEFLATED )
    zip.write(zip_name)
    zip.close()
    print ('compressing finished')
#读取本地txt文件，json的格式化
def data_read(file):
    with open(file,'r') as f:
        data_li = f.readlines()
        row_list = []
        for data in data_li:
            json_str = json.loads(data)
            try:
                data_list = json_str['tick']['data']
            except:
                pass
            else:
                for data in data_list:
                    price = data['price']
                    amount = data['amount']
                    direction = data['direction']
                    ts = json_str['tick']['ts']
                    order_id = json_str['tick']['id']
                    order_ts = json_str['tick']['ts']
                    butts = json_str['butts']
                    exchange_ts = json_str['ts']
                    list =["huobi","btc","usdt",price,amount,direction,order_id,order_ts,order_id,ts,butts,exchange_ts]
                    row_list.append(list)
        return row_list

if __name__ == '__main__':
    file = 'trade_btcusdt.log'
    row_list = data_read(file)
    date_name = str(time.strftime("%Y-%m-%d"))
    csv_path = "./csv_files/"+"trade_data_huobi" + date_name + ".csv"
    csv_write(row_list,csv_path)
    zip_files(csv_path)