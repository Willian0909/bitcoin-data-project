#-*- encoding:utf-8 -*-
import csv
import zipfile
import json
import time

#写入csv文件
def csv_write(list,file_name):
       with open(file_name,"a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['exchange','trade_currency','base_currency','type','start_from','start_from_ms','open','low','high','close','volume','amount','count','exchange_ts','butts'])
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
            print(data)
            json_str = json.loads(data)
            startfrom = json_str['tick']['id']
            startfrom_ms = int(json_str['tick']['id'])*1000
            type = json_str['ch'].split('.')[3]
            op = json_str['tick']['open']
            low = json_str['tick']['low']
            high = json_str['tick']['high']
            close = json_str['tick']['close']
            volume= json_str['tick']['vol']
            amount= json_str['tick']['amount']
            count= json_str['tick']['count']
            exchange_ts = json_str['ts']
            butts = json_str['butts']
            list =["huobi","btc","usdt",type,startfrom,startfrom_ms,op,low,high,close,volume,amount,count,exchange_ts,butts]
            row_list.append(list)
        return row_list

if __name__ == '__main__':
    file = 'btcusdt_2018-07-12.log'
    row_list = data_read(file)
    date_name = str(time.strftime("%Y-%m-%d"))
    csv_path = "./csv_files/"+"kline_data_huobi" + date_name + ".csv"
    print(row_list)
    csv_write(row_list,csv_path)
    zip_files(csv_path)