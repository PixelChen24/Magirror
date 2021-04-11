# -*- coding:utf-8 -*-
import time
list=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

def getTime():  # 获取一个格式标准的时间 hour:minute:sec
    localtime = time.localtime(time.time())
    hour = localtime.tm_hour
    minute = localtime.tm_min

    # 下面进行标准化格式时间
    if hour<10:
        Hour='0'+str(hour)
    else:
        Hour=str(hour)
    if minute < 10:
        Minute = '0' + str(minute)  # 如果分钟只有一位，那么自动补零
    else:
        Minute = str(minute)
    Time = Hour + ':' + Minute
    return Time

def getDate():# 获取一个标准格式的日期 Month/Day
    localtime = time.localtime(time.time())
    month=localtime.tm_mon
    day=localtime.tm_mday
    Date=str(month)+'/'+str(day)
    return Date

def getYear():
    localtime=time.localtime(time.time())
    return localtime.tm_year

def getMonth():
    localtime = time.localtime(time.time())
    return localtime.tm_mon

def getDay():
    localtime = time.localtime(time.time())
    return localtime.tm_mday

def getHour():
    localtime = time.localtime(time.time())
    return localtime.tm_hour

def getMinute():
    localtime = time.localtime(time.time())
    return localtime.tm_min

def getSec():
    localtime = time.localtime(time.time())
    return localtime.tm_sec

def getWday():
    localtime=time.localtime(time.time())
    return localtime.tm_wday
def getWeekday():
    localtime=time.localtime(time.time())
    XingQi = localtime.tm_wday
    XingQi = list[XingQi]
    return XingQi