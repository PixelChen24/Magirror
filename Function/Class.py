# -*- coding:utf-8 -*-
import os
import datetime
import time
from Function import Time
WeekdayList=["星期一","星期二","星期三",'星期四','星期五','星期六','星期日']


begin=datetime.datetime(2021,3,1)
today=datetime.datetime(Time.getYear(),Time.getMonth(),Time.getDay())
interval=today-begin
interval=interval.days#今天距离标准日期的间隔天数
weekcount=interval//7+1


table={
    '星期一':{
        1:{"course":"建设项目管理","range":range(9,17),"room":"文泰219"},
        2:{"course":"线性代数","range":range(1,17),"room":"文泰301"},
        3:{"course":"体育专项","range":range(1,17),"room":"小球馆乒乓球场17-32"},
        4:{"course":"项目管理原理","range":range(1,9),"room":"文泰301"},
        5:{"course":"形势与政策","range":range(1,5),"room":"文波211"}
    },
    '星期二':{
        1:{"course":"无课程","range":range(0,0),"room":"文泰219"},
        2:{"course":"工程经济学","range":range(1,17),"room":"文泰310"},
        3:{"course":"土木工程概论","range":range(1,9),"room":"文泰112"},
        4:{"course":"房地产金融(双语)","range":range(1,17),"room":"文泰109"},
        5:{"course":"以案说法","range":range(1,17),"room":"文波211"}
    },
    '星期三':{
        1:{"course":"项目管理原理","range":range(1,9),"room":"文泰301"},
        2:{"course":"房地产开发","range":range(1,17),"room":"文波205"},
        3:{"course":"无课程","range":range(0,0),"room":"小球馆乒乓球场17-32"},
        4:{"course":"土木工程概论","range":range(1,9),"room":"文泰112"},
        5:{"course":"无课程","range":range(0,0),"room":"文波211"}
    },
    '星期四':{
        1:{"course":"无课程","range":range(0,0),"room":"文泰219"},
        2:{"course":"会计学","range":range(1,17),"room":"文波207"},
        3:{"course":"无课程","range":range(0,0),"room":"小球馆乒乓球场17-32"},
        4:{"course":"无课程","range":range(0,0),"room":"文泰301"},
        5:{"course":"无课程","range":range(0,0),"room":"文波211"}
    },
    '星期五':{
        1:{"course":"建设项目管理","range":range(9,17),"room":"文泰219"},
        2:{"course":"建筑识图","range":range(1,17),"room":"文泉104"},
        3:{"course":"城市土地市场","range":range(1,17),"room":"文泰101"},
        4:{"course":"无课程","range":range(0,0),"room":"文泰301"},
        5:{"course":"无课程","range":range(0,0),"room":"文波211"}
    }
}

def getClass(Number,WeekDay):#获取今天第Number节课的信息
    if weekcount in table[WeekDay][Number]["range"]:
        return table[WeekDay][Number]
    else:
        returnMessage=dict()
        returnMessage['course']='无课程'
        return returnMessage
