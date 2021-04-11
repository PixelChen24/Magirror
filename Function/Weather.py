# -*- coding:utf-8 -*-
import requests

LOCATION = requests.get('https://checkip.amazonaws.com').text.strip()#获取本机ip地址
KEY = '在此处输入你的对应心知API秘钥'  # API key 心知天气

currentWeatherAPI='https://api.seniverse.com/v3/weather/now.json'
dailyAPI = 'https://api.seniverse.com/v3/weather/daily.json'#获取五天天气预报
AQIAPI='https://api.seniverse.com/v3/air/now.json'#获取空气污染指数（心知天气免费用户没有此权限！）
suggestionAPI='https://api.seniverse.com/v3/life/suggestion.json'#获取生活建议
UNIT = 'c'  # 单位摄氏度
LANGUAGE = 'zh-Hans'#数据返回格式为中文


def getWeather():#根据IP地址获取五日天气预报
    try:
        result = requests.get(dailyAPI, params={
            'key': KEY,
            'location': LOCATION,
            'language': LANGUAGE,
            'unit': UNIT
        }, timeout=2)
        result = eval(result.text)
        info = result['results'][0]['daily']
        returnMessage = {}
        returnMessage['City'] = result['results'][0]['location']['name']
        returnMessage['TodayTemp'] = info[0]['low'] + '~' + info[0]['high'] + '℃'
        returnMessage['TodayInfo'] = {}
        returnMessage['TodayInfo']['日间天气'] = info[0]['text_day']
        returnMessage['TodayInfo']['日间天气代码'] = info[0]['code_day']
        returnMessage['TodayInfo']['夜间天气'] = info[0]['text_night']
        returnMessage['TodayInfo']['夜间天气代码'] = info[0]['code_night']
        returnMessage['TodayInfo']['空气湿度'] = info[0]['humidity']

        returnMessage['More'] = []
        for i in range(0, 3):  # 存储更多四日天气
            returnMessage['More'].append([info[i]['text_day'], info[i]['low'] + '~' + info[i]['high'] + '℃'])
        return returnMessage
    except:
        return '0.O好像。。出错了？'

def getCurrentWeather():
    try:
        result = requests.get(currentWeatherAPI, params={
            'key': KEY,
            'location': LOCATION,
            'language': LANGUAGE,
            'unit': UNIT
        }, timeout=2)
        result = eval(result.text)
        temperature = result['results'][0]['now']['temperature']
        return temperature

    except:
        return '0.O好像。。出错了？'


def getAQI():#获取空气质量信息（心知天气免费用户无此权限）
    try:
        result = requests.get(AQIAPI, params={
            'key': KEY,
            'location': LOCATION,
            'language': LANGUAGE,
            'scope': ''
        }, timeout=1)
        result = eval(result.text)
        #info = result['results'][0]['daily']
        return result
    except:
        return '0.O好像。。出错了？'

def getSuggestion():#获取生活指南
    try:
        result = requests.get(suggestionAPI, params={
            'key': KEY,
            'location': LOCATION,
            'language': LANGUAGE,
            'unit': UNIT
        }, timeout=1)
        result=eval(result.text)
        suggestions=''
        suggestionsList=result['results'][0]['suggestion']
        return suggestionsList
    except:
        return '0.O好像。。出错了？'

