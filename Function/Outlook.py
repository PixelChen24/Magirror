import yaml
import requests
import msal
import datetime

file_stream = open('Function/OutlookConfig.yml', 'r')
config = yaml.load(file_stream, yaml.SafeLoader)  # 加载Outlook配置文件
refresh_token=config['refresh_token']
token=refresh_token

events={}


def get_msal_app(cache=None):
    """
    通过SDK实例化一个应用程序

    :param cache:
    :return: APP
    """
    # Initialize the MSAL confidential client
    auth_app = msal.ConfidentialClientApplication(
        config['client_id'],
        authority=config['authority'],
        client_credential=config['client_secret'],
        token_cache=cache)
    return auth_app


def get_new_token()->str:
    """
    获取访问令牌(token)
    此处采用refresh_token的机制获取新的token。在一台设备上使用网页授权登录后会产生一个token以及对应的refresh_token,
    对于之后的访问，不需要重新申请token，只要从最初的refresh_token生成token就好。
    一般来说，只要不清除系统缓存/浏览器缓存，refresh_token长期有效

    :return: 令牌
    """
    global token,refresh_token
    app=get_msal_app()
    refresh_info=app.acquire_token_by_refresh_token(refresh_token=refresh_token,scopes=config['scopes'])
    token=refresh_info['access_token']
    # refresh_token=refresh_token['refresh_token']
    return token


def get_date(shift_day=0,shift_hour=0)->str:
    """
    构造日期，格式为yyyy-mm-ddThh:mm:ss+08:00，例如2022-01-05T00:00:00+08:00\n
    默认返回系统当前的时间。通常被用作指定日期的左临界点。\n
    通过赋值shift_day和shift_hour,产生以今天为基准的偏移时间。通常被用作指定日期的右临界点。\n

    :param shift_day: 天偏移量
    :param shift_hour: 小时偏移量
    :return: 格式化的日期
    """
    today=datetime.datetime.now()
    shift_day=datetime.timedelta(days=shift_day,hours=shift_hour)+today
    year=shift_day.year
    month=shift_day.month
    day=shift_day.day
    if month<10:
        month="0"+str(month)
    if day<10:
        day="0"+str(day)
    date=str(year)+"-"+str(month)+"-"+str(day)+"T"+"00"+":"+"00:00+08:00"  # +08:00是因为北京时间UTC+8
    return date


def get_calendar_events(start=get_date(), end=get_date(shift_day=3),
                        timezone="China Standard Time"):
    """
    调用Graph API 获取指定时间范围内用户的日历\n
    返回信息包括：事件名、开始时间、结束时间、地点

    :param start: 查询开始的时间 format:yyyy-mm-ddThh:mm:ss+08:00
    :param end: 查询结束的时间 format:yyyy-mm-ddThh:mm:ss+08:00
    :param timezone: 时区，默认北京时间UTC+8
    :return: 事件
    """
    global events
    Token = get_new_token()
    headers = {
        'Authorization': 'Bearer {0}'.format(Token),
        'Prefer': 'outlook.timezone="{0}"'.format(timezone)
    }
    query_params = {
        'startDateTime': start,
        'endDateTime': end,
        '$select': 'subject,organizer,start,end,location',
        '$orderby': 'start/dateTime',
        '$top': '50'
    }
    events = requests.get('{0}/me/calendarview'.format(config['graph_api']),
                          headers=headers,
                          params=query_params)
    events=events.json()
    print("Get Outlook events successfully.")
    return events


def analyse_events(events:dict):
    """
    将API返回的信息格式化

    :param events: get_calendar_events()的返回数据
    :return: 格式化的事件列表
    """
    return_val=[]
    events_list=events['value']
    events_num=len(events_list)
    if events_num==0:
        return []
    for item in events_list:
        subject=item['subject']
        start_time=item['start']['dateTime']
        end_time=item['end']['dateTime']
        location=item['location']['displayName']
        one=dict()
        one['subject']=subject
        one['start_time']=start_time
        one['end_time']=end_time
        one['location']=location
        return_val.append(one)
    return return_val


def analyse_date(format_date:str):
    date=format_date.split('T')[0]
    time=format_date.split('T')[1]
    month=date.split('-')[1]
    day=date.split('-')[2]
    hour=time.split(':')[0]
    minute=time.split(':')[1]
    return month+'月'+day+'日',hour+':'+minute


if __name__=="__main__":
    print(analyse_date(analyse_events(get_calendar_events(get_date(),get_date(1)))[0]["start_time"]))