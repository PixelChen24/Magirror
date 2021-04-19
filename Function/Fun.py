# -*- coding:utf-8 -*-
import requests
import random
from Function import Time

HistoryKey = '在此处输入你的对应请求KEY'  # 聚合数据——历史上的今天
HistoryURL = 'http://v.juhe.cn/todayOnhistory/queryEvent.php'

NewsKey = '在此处输入你的对应请求KEY'  # 聚合数据——头条新闻
NewsURL = 'http://v.juhe.cn/toutiao/index'

LunarKey='在此处输入你的对应请求KEY'#聚合数据_万年历
LunarURL='http://v.juhe.cn/calendar/day'

SentenceURL="https://v1.hitokoto.cn/?c="
SentenceType=['c','d','e','h','i','k'] #根据个人喜好加入a-l参数
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
        return dateName + ' : ' + chosenEvent  # 数据返回格式为日期+事件
    except:
        return '0.O好像。。出错了？'


def getNews(type):#获取type类型的新闻（新闻质量堪忧）
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
        return chosenNews + '    来源: ' + authName  # 数据返回格式为日期+事件
    except:
        return '0.O好像。。出错了？'


def getHot():#获取百度热搜前三
    try:
        newsList = requests.get('http://top.baidu.com/mobile_v2/buzz/hotspot/')
        newsList=eval(newsList.text)
        top3=[]
        for i in range(0,3):
            top3.append(newsList['result']['topwords'][i]['keyword'])
        return top3
    except:
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
        return result['result']['data']['lunarYear']+' '+result['result']['data']['lunar']
    except:
        return '获取农历失败'

def getHoliday():
    Date=str(Time.getYear())+'-'+str(Time.getMonth())+'-'+str(Time.getDay())
    try:
        result = requests.get(LunarURL, params={
            'key': LunarKey,
            'date': Date
        }, timeout=5)
        result = eval(result.text)  # 若请求结果为Resonse<200>，那么可以尝试.text来访问
        return result['result']['data']['holiday']
    except:
        return '无节日'

def getSentence():
    try:
        typecnt=len(SentenceType)
        chosenType = SentenceType[random.randint(0, typecnt-1)]
        QueryURL = SentenceURL + chosenType
        result = requests.get(QueryURL).text
        NewResult=result.replace('null','\'佚名\'')
        result = eval(NewResult)
        return '「'+result['hitokoto']+'」'
    except:
        return '谁都会犯错，魔镜也不例外。'
