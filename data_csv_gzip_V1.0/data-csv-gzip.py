#-*- encoding:utf-8 -*-
import csv
import zipfile
import json
import time

class Trade(object):
#写入csv文件
    def csv_write(self,list,file_name):
           with open(file_name,"a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['exchange','trade_currency','base_currency','price','amount','direction','order_id','order_ts','id','ts','butts','exchange_ts'])
            writer.writerows(list)
    #压缩文件
    def zip_files(self,zip_name ):
        zip = zipfile.ZipFile( zip_name +".gz", 'w', zipfile.ZIP_DEFLATED )
        zip.write(zip_name)
        zip.close()
        print ('compressing finished')
    #读取本地txt文件，json的格式化
    def data_read(self,file):
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

class Depth(object):
#写入csv文件
    def csv_write(self,list,file_name):
           with open(file_name,"a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['exchange','trade_currency','base_currency','asks','bids','timestamp', 'exchange_ts','butts'])
            writer.writerows(list)
    #压缩文件
    def zip_files(self,zip_name ):
        zip = zipfile.ZipFile( zip_name+".gz", 'w', zipfile.ZIP_DEFLATED )
        zip.write(zip_name)
        zip.close()
        print ('compressing finished')
    #读取本地txt文件，json的格式化
    def data_read(self,file):
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

class Kline(object):
#写入csv文件
    def csv_write(self,list,file_name):
           with open(file_name,"a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['exchange','trade_currency','base_currency','type','start_from','start_from_ms','open','low','high','close','volume','amount','count','exchange_ts','butts'])
            writer.writerows(list)
    #压缩文件
    def zip_files(self,zip_name ):
        zip = zipfile.ZipFile( zip_name+".gz", 'w', zipfile.ZIP_DEFLATED )
        zip.write(zip_name)
        zip.close()
        print ('compressing finished')
    #读取本地txt文件，json的格式化
    def data_read(self,file):
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

class Tiker(object):
#写入csv文件
    def csv_write(self,list,file_name):
           with open(file_name,"a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['exchange','trade_currency','base_currency','timestamp','open','high','low','close','volume','amount','count','butts'])
            writer.writerows(list)
    #压缩文件
    def zip_files(self,zip_name ):
        zip = zipfile.ZipFile( zip_name+".gz", 'w', zipfile.ZIP_DEFLATED )
        zip.write(zip_name)
        zip.close()
        print ('compressing finished')
    #读取本地txt文件，json的格式化
    def data_read(self,file):
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
    file = 'depthbtcusdt12.log'
    trade = Trade()
    depth = Depth()
    kline = Kline()
    tiker = Tiker()
    if file.startswith("trade"):
        row_list = trade.data_read(file)
        date_name = str(time.strftime("%Y-%m-%d"))
        csv_path = "./csv_files/"+"trade_data_huobi" + date_name + ".csv"
        trade.csv_write(row_list,csv_path)
        trade.zip_files(csv_path)
    elif file.startswith("depth"):
        row_list = depth.data_read(file)
        date_name = str(time.strftime("%Y-%m-%d"))
        csv_path = "./csv_files/" + "depth_data_huobi_" + date_name + ".csv"
        depth.csv_write(row_list, csv_path)
        depth.zip_files(csv_path)
    elif file.endswith("kline"):
        row_list = kline.data_read(file)
        date_name = str(time.strftime("%Y-%m-%d"))
        csv_path = "./csv_files/" + "kline_data_huobi_" + date_name + ".csv"
        kline.csv_write(row_list, csv_path)
        kline.zip_files(csv_path)
    else:
        row_list = tiker.data_read(file)
        date_name = str(time.strftime("%Y-%m-%d"))
        csv_path = "./csv_files/" + "tiker_data_huobi_" + date_name + ".csv"
        tiker.csv_write(row_list, csv_path)
        tiker.zip_files(csv_path)

