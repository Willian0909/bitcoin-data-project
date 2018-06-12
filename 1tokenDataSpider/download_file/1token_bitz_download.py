# -*- coding:utf-8 -*-
import re
import requests
import time
def get(url):
    for i in  range(99999):
        try:
            response = requests.get(url,timeout=300)
            ret = response.content
        except:

            time.sleep(1)
        else:
            u_date = re.findall(r'date=(.*)&', url)[0].replace('&', '').replace('contract=', '-').replace('/', '-')
            # print('正在获取'+u_date+'的数据')
            file_name = './bitz' + '/' + u_date + '.gz'
            with open(file_name,'wb') as f:
                f.write(ret)
                break

with open('bitz.txt', 'r') as f:

    date = f.readlines()
    for dt in date:
        url = dt.replace('\n', '')
        if url[0]=="?":
            continue
        else:
            print(url)
            get(url)