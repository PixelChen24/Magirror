# -*- coding:utf-8 -*-
import requests
import yaml
filestream=open("Function/APIConfig.yml",'r')
APIConfig=yaml.load(filestream,yaml.SafeLoader)
LOCATION = requests.get('https://checkip.amazonaws.com').text.strip()#获取本机ip地址
# LOCATION='西安'  # 如果你使用了代理，那么请手动指定城市
print("Welcome my friend from ",LOCATION)
KEY = APIConfig['WeatherKEY']
UID = APIConfig['WeatherUID']  # 用户ID

currentWeatherAPI=APIConfig['currentWeatherAPI']
dailyAPI = APIConfig['dailyAPI']  # 获取五天天气预报
AQIAPI = APIConfig['AQIAPI']  # 获取空气污染指数
suggestionAPI = APIConfig['suggestionAPI']  # 获取生活建议
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
        print("Get weather details successfully.")
        return returnMessage
    except:
        print("**Get weather detail failed.**")
        returnMessage={}
        returnMessage['City']='x'
        returnMessage['TodayTemp']='x'
        returnMessage['TodayInfo'] = {}
        returnMessage['TodayInfo']['日间天气'] = 'x'
        returnMessage['TodayInfo']['日间天气代码'] = '0'
        returnMessage['TodayInfo']['夜间天气'] = 'x'
        returnMessage['TodayInfo']['夜间天气代码'] = '0'
        returnMessage['TodayInfo']['空气湿度'] = 'x'
        returnMessage['More']=[]
        for i in range(3):
            tempList=[]
            tempList.append('x')
            tempList.append('x')
            returnMessage['More'].append(tempList)
        return returnMessage


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
        print('Get current weather successfully.')
        return temperature

    except:
        print("**Get current weather failed.**")
        return '0'


def getAQI():#获取空气质量信息（暂无权限开通）
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
        suggestionsList=result['results'][0]['suggestion']
        print("Get suggestions successfully.")
        return suggestionsList
    except:
        print("**Get suggestions failed.**")
        suggestionsList={}
        suggestionsList['uv']={}
        suggestionsList['uv']['brief']='x'

        suggestionsList['dressing'] = {}
        suggestionsList['dressing']['brief'] = 'x'

        suggestionsList['sport'] = {}
        suggestionsList['sport']['brief'] = 'x'

        suggestionsList['flu'] = {}
        suggestionsList['flu']['brief'] = 'x'
        return suggestionsList


if __name__=='__main__':
    result = requests.get(currentWeatherAPI, params={
        'key': KEY,
        'location': LOCATION,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=2)
    result = eval(result.text)
    print(result)