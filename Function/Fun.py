# -*- coding:utf-8 -*-
import requests
import random
import yaml
from Function import Time

filestream=open('Function/APIConfig.yml','r')
APIConfig=yaml.load(filestream,yaml.SafeLoader)

HistoryKey = APIConfig['HistoryKey']  # 聚合数据——历史上的今天
HistoryURL = APIConfig['HistoryURL']

NewsKey = APIConfig['NewsKey']  # 聚合数据——头条新闻
NewsURL = APIConfig['NewsURL']

LunarKey=APIConfig['LunarKey']#聚合数据_万年历
LunarURL=APIConfig['LunarURL']

SentenceURL="https://v1.hitokoto.cn/?c="
SentenceType=['c','d','e','h','i','k']


def getHistory(Date):#获取历史上的今天
    try:
        result = requests.get(HistoryURL, params={
            'key': HistoryKey,
            'date': Date
        }, timeout=5)
        result = eval(result.text)  # 若请求结果为Resonse<200>，那么可以尝试.text来访问
        events = result['result']  # 事件列表
        eventCount = len(events)  # 事件个数
        chosenIndex = random.randint(0, eventCount - 1)  # 生成一个随机索引
        chosenEvent = events[chosenIndex]['title']  # 通过随机索引访问一个事件
        dateName = events[chosenIndex]['date']
        print("Get history successfully.")
        return dateName + ' : ' + chosenEvent  # 数据返回格式为日期+事件
    except:
        print("**Get history failed.**")
        return '0.O好像。。出错了？'


def getNews(type): # 获取type类型的新闻（新闻质量堪忧）
    try:
        result = requests.get(NewsURL, params={
            'key': NewsKey,
            'type': type
        }, timeout=5)
        result = eval(result.text)  # 若请求结果为Resonse<200>，那么可以尝试.text来访问
        print(result)
        newsList = result['result']['data']  # 新闻列表
        newsCount = len(newsList)  # 事件个数
        chosenIndex = random.randint(0, newsCount - 1)  # 生成一个随机索引
        chosenNews = newsList[chosenIndex]['title']  # 通过随机索引访问一个事件
        authName = newsList[chosenIndex]['author_name']
        print("Get news successfully.")
        return chosenNews + '    来源: ' + authName  # 数据返回格式为日期+事件
    except:
        print("**Get news failed.**")
        return '0.O好像。。出错了？'


def getHot():#获取百度热搜前三
    try:
        newsList = requests.get('http://top.baidu.com/mobile_v2/buzz/hotspot/')
        newsList=eval(newsList.text)
        top3=[]
        for i in range(0,3):
            top3.append(newsList['result']['topwords'][i]['keyword'])
        print("Get Baidu news successfully.")
        return top3
    except:
        print("**Get Baidu news failed.**")
        top3=[]
        top3.append('获取百度热点失败')
        top3.append('获取百度热点失败')
        top3.append('获取百度热点失败')
        return top3


def getLunar():
    Date=str(Time.getYear())+'-'+str(Time.getMonth())+'-'+str(Time.getDay())
    try:
        result = requests.get(LunarURL, params={
            'key': LunarKey,
            'date': Date
        }, timeout=5)
        result = eval(result.text)  # 若请求结果为Resonse<200>，那么可以尝试.text来访问
        print("Get lunar information successfully.")
        return result['result']['data']['lunarYear']+' '+result['result']['data']['lunar']
    except:
        print("**Get lunar information failed.**")
        return '获取农历失败'


def getHoliday():
    Date=str(Time.getYear())+'-'+str(Time.getMonth())+'-'+str(Time.getDay())
    try:
        result = requests.get(LunarURL, params={
            'key': LunarKey,
            'date': Date
        }, timeout=5)
        result = eval(result.text)  # 若请求结果为Resonse<200>，那么可以尝试.text来访问
        print("Get holiday successfully.")
        return result['result']['data']['holiday']
    except:
        print("**Get holiday failed or empty holiday.**")
        return '无节日'


def getSentence():
    try:
        chosenType = SentenceType[random.randint(0, 5)]
        QueryURL = SentenceURL + chosenType
        result = requests.get(QueryURL).text
        NewResult=result.replace('null','\'佚名\'')
        result = eval(NewResult)
        print("Get sentence successfully.")
        return '「'+result['hitokoto']+'」'
    except:
        print("**Get sentence failed.**")
        return '谁都会犯错，魔镜也不例外。'
