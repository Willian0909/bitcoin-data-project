#-*- encoding:utf-8 -*-
import csv
import zipfile
import json
import time

#写入csv文件
def csv_write(list,file_name):
       with open(file_name,"a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['exchange','trade_currency','base_currency','asks','bids','timestamp', 'exchange_ts','butts'])
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
            asks = json_str["tick"]["asks"]
            bids = json_str["tick"]["bids"]
            timestamp = json_str["tick"]["ts"]
            exchange_ts = json_str['ts']
            butts = json_str['butts']
            list =["huobi","btc","usdt",asks,bids,timestamp,exchange_ts,butts]
            row_list.append(list)
        return row_list

if __name__ == '__main__':

    file = 'depthbtcusdt12.log'
    row_list = data_read(file)
    date_name = str(time.strftime("%Y-%m-%d"))
    csv_path = "./csv_files/"+"depth_data_huobi_" + date_name + ".csv"
    csv_write(row_list,csv_path)
    zip_files(csv_path)