# -*- coding: utf-8 -*-
# 日期ｌｉｓｔ的生成
def date_handle():
    years = ['2016','2017']
    month = ['01','02','03','04','05','06','07','08','09','10','11','12']
    days= ['31','28','31','30','31','30','31','31','30','31','30','31']
    date_list = []
    for y in years:
        for m in month:
            count = 1
            for day in range(1,int(days[month.index(m)])+1):
                count+=1
                if count<11:
                    dy = '0'+str(day)
                    date = y +'-'+ m + '-'+dy
                    date_list.append(date)
                else:
                    date = y + '-' + m + '-' + str(day)
                    date_list.append(date)

    start_time = str(input("请输入起始日期(日期格式：xxxx-xx-xx)："))
    end_time = str(input("请输入结束日期(日期格式：xxxx-xx-xx)："))
    new_list = []
    for index in range(date_list.index(start_time),date_list.index(end_time)):
        new_list.append(date_list[index])
    # for dt in date_list:
    #     print(dt)
    new_list.reverse()
    # return new_list
    with open('date-list.txt','w') as f:
        f.write(str(new_list))
date_handle()