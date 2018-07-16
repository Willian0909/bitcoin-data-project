#-*- encoding:utf-8 -*-
import csv
import zipfile
import json
import time

#写入csv文件
def csv_write(list,file_name):
       with open(file_name,"a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['exchange','trade_currency','base_currency','timestamp','open','high','low','close','volume','amount','count','butts'])
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
            timestamp = json_str['ts']
            op = json_str['tick']['open']
            low = json_str['tick']['low']
            high = json_str['tick']['high']
            close = json_str['tick']['close']
            volume= json_str['tick']['vol']
            amount= json_str['tick']['amount']
            count= json_str['tick']['count']
            butts = json_str['butts']
            list =["huobi","btc","usdt",timestamp,op,high,low,close,volume,amount,count,butts]
            row_list.append(list)
        return row_list

if __name__ == '__main__':
    file = 'tike_btcusdt.log'
    row_list = data_read(file)
    date_name = str(time.strftime("%Y-%m-%d"))
    csv_path = "./csv_files/"+"tiker_data_huobi" + date_name + ".csv"
    print(row_list)
    csv_write(row_list,csv_path)
    zip_files(csv_path)