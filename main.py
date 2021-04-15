# -*- coding:utf-8 -*-
ver = 'Version: v1.2.0'
import pygame
import sys
import random
#sys.path.append("/media/pixelchen/OS/Users/chen/source/repos/赵小姐的魔镜/")
import os
import time
from Function import Time, Fun, Weather, Class
import QR
from pygame.locals import *
import pygame.freetype

weatherList = ["日间晴", "夜间晴", "日间晴", "夜间晴", "多云", "晴间多云", "晴间多云", "大部多云", "大部多云", "阴", "阵雨", "雷阵雨", "雷阵雨伴有冰雹",
               "小雨", "中雨", "大雨", "暴雨", "大暴雨", "特大暴雨", "冻雨", "雨夹雪", "阵雪", "小雪", "中雪", "大雪", "暴雪",
               "浮尘", "扬沙", "沙尘暴", "强沙尘暴", "雾", "霾", "风", "大风", "飓风", "热带风暴", "龙卷风", "冷", "热", "未知"]

WeatherMessage = {}
HistoryMessage = ''
SuggestionMessage = {}
Holiday='无节日'
Lunar='辛丑年二月廿七'
currentTemp=0
Hot=[]
ZhuanLanTitle=''
ZhuanLanDate=''
DailySentence=''

FPS=30
alpha=100
pygame.init()
screen = pygame.display.set_mode((1080, 1920),FULLSCREEN)
pygame.display.set_caption("MagicMirror")
clock=pygame.time.Clock()
WallPaper=pygame.image.load("Background/1080p.png")
WallPaper.set_alpha(255)
CutPaper=pygame.image.load("Background/CutBackground.png")
CutPaper.set_alpha(alpha//2)
def getWeatherIcon(WeatherCode, size):
    fileName = WeatherCode + '@' + str(size) + 'x' + '.png'
    wholePath = 'WeatherIcon/black/' + fileName
    icon = pygame.image.load(wholePath)
    return icon


def updateAPI():
    global HistoryMessage
    global WeatherMessage
    global SuggestionMessage
    global currentTemp
    global Holiday
    global Lunar
    global Hot
    global ZhuanLanTitle
    global ZhuanLanDate
    global DailySentence
    HistoryMessage = Fun.getHistory(Time.getDate())
    WeatherMessage = Weather.getWeather()
    SuggestionMessage = Weather.getSuggestion()
    currentTemp=Weather.getCurrentWeather()
    Holiday=Fun.getHoliday()
    if Holiday=='':
        Holiday='无节日'
    if Time.getMonth()==4 and Time.getDay()==29:
        Holiday='我的生日'
    Lunar=Fun.getLunar()
    Hot=Fun.getHot()
    ZhuanLanTitle,ZhuanLanDate= QR.getQR()
    DailySentence=Fun.getSentence()


def WhetherToUpdate():  # 每天是否访问管理，用于节省API调用次数以及程序运行效率
    isVisited = False  # 默认今天访问过了
    todayVisitedFile = open("BufferData/Visited.txt")  # 这个文件存储访问情况，每行是一个日期，代表该日期访问过，新的日期加在列表头部
    todayVisitedLine = todayVisitedFile.readline()  # 按行读取
    visitedList = []
    while 1:
        if not todayVisitedLine:
            break
        visitedList.append(todayVisitedLine)
        todayVisitedLine = todayVisitedFile.readline()
    todayDate = str(str(Time.getYear()) + '/' + Time.getDate()) + '\n'

    if visitedList[0] != todayDate:  # 今天并没有访问过
        visitedList.insert(0, todayDate)
        savefile = open("BufferData/Visited.txt", "w")
        saveline = []
        for lines in visitedList:
            savefile.write(lines)  # 系统读取的时候默认带换行符，不需要再加
        savefile.close()
        print("更新状态成功")
    else:
        print("今天访问过了")



def loadGif(dirname, left, top):
    wholename = 'Gifs/' + dirname
    path = os.listdir(wholename)
    path.sort(key=lambda x: int(x[4:-4]))  # 默认的顺序是随机的，要使用正则表达式排序
    count = len(path)
    for picNmame in path:
        pic = pygame.image.load(wholename + '/' + picNmame)
        picRect = pic.get_rect()
        picRect.left = left
        picRect.top = top
        screen.blit(pic, picRect)
        pygame.display.update()
        time.sleep(1.0 / count)


def showTime():
    global Lunar
    global Holiday
    font = pygame.freetype.Font('./FontLib/setup/苹方黑体-中粗-简.ttf', 192)
    FormatTime = Time.getTime()
    font.render_to(screen, (50, 100), FormatTime, (255, 255, 255))  # 时间

    year = str(Time.getYear())
    month = str(Time.getMonth())
    day = str(Time.getDay())
    XingQi = Time.getWeekday()
    Date = year + '年' + month + '月' + day + '日' + '    ' + XingQi  # 日期
    dateFont = pygame.freetype.Font('./FontLib/setup/苹方黑体-准-简.ttf', 36)
    dateFont.render_to(screen, (100, 260), Date, (255, 255, 255))
    dateFont.render_to(screen, (140, 300), Lunar, (255, 255, 255))

    HolidayIcon=pygame.image.load("FunIcon/Holiday.png")
    HolidayIconRect=HolidayIcon.get_rect()
    HolidayIconRect.center=(100,400)

    newRect=HolidayIconRect.inflate(24,24)
    dateFont.render_to(screen,(220,380),Holiday,(255,255,255))
    screen.blit(HolidayIcon,HolidayIconRect)



def showMainWeather():
    global currentTemp
    if Time.getHour() in range(5, 18):
        TodayDayIcon = getWeatherIcon(WeatherMessage['TodayInfo']['日间天气代码'], 2)
        TodayDayIconRect = TodayDayIcon.get_rect()
        TodayDayIconRect.left = 820
        TodayDayIconRect.top = 110
        screen.blit(TodayDayIcon, TodayDayIconRect)

        WeatherFont = pygame.freetype.Font('FontLib/setup/苹方黑体-准-简.ttf', 32)
        WeatherFont.render_to(screen, (948, 100), WeatherMessage['TodayInfo']['日间天气'],(255,255,240))

        NightFont=pygame.freetype.Font('FontLib/setup/苹方黑体-准-简.ttf', 24)
        NightFont.render_to(screen, (888, 325), '夜间:'+WeatherMessage['TodayInfo']['夜间天气'], (65,105,225))
    else:
        TodayNightIcon = getWeatherIcon(WeatherMessage['TodayInfo']['夜间天气代码'], 2)
        TodayNightIconRect = TodayNightIcon.get_rect()
        TodayNightIconRect.left = 820
        TodayNightIconRect.top = 110
        screen.blit(TodayNightIcon, TodayNightIconRect)

        WeatherFont = pygame.freetype.Font('FontLib/setup/苹方黑体-准-简.ttf', 48)
        WeatherFont.render_to(screen, (948, 100), WeatherMessage['TodayInfo']['夜间天气'],(255,255,240))

    city=WeatherMessage['City']
    cityFont=pygame.freetype.Font('FontLib/setup/苹方黑体-细-繁.ttf',32)
    cityFont.render_to(screen,(630+48,100),city+'市',(255,255,255))



    Point=pygame.image.load("FunIcon/Point.png")
    PointRect=Point.get_rect()
    PointRect.left=590+48
    PointRect.top=100
    screen.blit(Point,PointRect)

    humiPic=pygame.image.load("WeatherIcon/Humi64.png")
    humiPicRect=humiPic.get_rect()
    humiPicRect.top=133
    humiPicRect.left=960
    screen.blit(humiPic,humiPicRect)


    if int(currentTemp)<20:
        COLOR=(135,206,250)
    elif int(currentTemp)<27 :
        COLOR=(127,255,170)
    elif int(currentTemp)<32:
        COLOR=(240,230,140)
    else:
        COLOR=(255,165,0)
    TempFont=pygame.freetype.Font('FontLib/setup/苹方黑体-中黑-简.ttf',96)
    TempFont.render_to(screen,(830,222),currentTemp+'℃',COLOR)

    HumidityFont=pygame.freetype.Font('FontLib/setup/苹方黑体-准-简.ttf',20)
    HumidityFont.render_to(screen,(968,133+40),WeatherMessage['TodayInfo']['空气湿度'],(0,0,0))


    SuggestionFont=pygame.freetype.Font('FontLib/setup/苹方黑体-准-简.ttf',24)
    UV=pygame.image.load('FunIcon/UV.png')
    UVRect=UV.get_rect()
    UVRect.left=590+48
    UVRect.top=165
    screen.blit(UV,UVRect)
    SuggestionFont.render_to(screen,(640+48,175),'UV:'+SuggestionMessage['uv']['brief'],(255,255,255))

    Cloth = pygame.image.load('FunIcon/Cloth.png')
    ClothRect = Cloth.get_rect()
    ClothRect.left = 590+48
    ClothRect.top = 215
    screen.blit(Cloth, ClothRect)
    SuggestionFont.render_to(screen, (640+48, 225), '穿衣:' + SuggestionMessage['dressing']['brief'], (255, 255, 255))

    Sport = pygame.image.load('FunIcon/sport.png')
    SportRect = Sport.get_rect()
    SportRect.left = 590+48
    SportRect.top = 265
    screen.blit(Sport, SportRect)
    SuggestionFont.render_to(screen, (640+48, 275), '运动:' + SuggestionMessage['sport']['brief'], (255, 255, 255))

    Sick = pygame.image.load('FunIcon/sick.png')
    SickRect = Sick.get_rect()
    SickRect.left = 590+48
    SickRect.top = 315
    screen.blit(Sick, SickRect)
    SuggestionFont.render_to(screen, (640+48, 325), '流感' + SuggestionMessage['flu']['brief'], (255, 255, 255))

def showMoreWeather():
    IntroFont = pygame.freetype.Font('FontLib/setup/苹方黑体-中粗-简.ttf', 32)
    IntroFont.render_to(screen,(814,380),"未来三日",(255,255,255))
    pygame.draw.line(screen,(255,255,255),(680,418),(1080,418))

    FutureFont = pygame.freetype.Font('FontLib/setup/苹方黑体-准-简.ttf', 32)
    for i in range(3):
        day=''
        if i==0:
            day='今天'
        if i==1:
            day='明天'
        if i==2:
            day='后天'
        FutureFont.render_to(screen,(680,426+i*35),day,(255,255,255))
        FutureFont.render_to(screen,(830,426+i*35),WeatherMessage['More'][i][0],(255,255,255))
        FutureFont.render_to(screen, (960, 426 + i * 35), WeatherMessage['More'][i][1], (255, 255, 255))

def showClass():
    ClassIcon=pygame.image.load("FunIcon/Class.png")
    ClassIconRect=ClassIcon.get_rect()
    ClassIconRect.center=(100,490)
    screen.blit(ClassIcon,ClassIconRect)
    TitleFont = pygame.freetype.Font('./FontLib/setup/苹方黑体-准-简.ttf', 48)
    TitleFont.render_to(screen,(211,460),"今日课程",(225,255,255))
    #pygame.draw.line(screen,(255,255,255),(75,518),(600,518))
    ClassFont=pygame.freetype.Font('./FontLib/setup/苹方黑体-准-简.ttf', 32)
    count = 0
    if Time.getWeekday()!='星期六' and Time.getWeekday()!='星期日':
        for i in range(1,6):
            if Class.getClass(i,Time.getWeekday())['course']!='无课程':
                ClassInfo=Class.getClass(i,Time.getWeekday())
                count+=1
                ClassFont.render_to(screen,(75,520+35*(count-1)),'第'+str(i)+'节:',(255,255,255))
                ClassFont.render_to(screen, (75+128, 520 + 35 * (count - 1)), ClassInfo['course'], (255, 255, 255))
                ClassFont.render_to(screen, (75+128+256, 520 + 35 * (count - 1)), ClassInfo['room'], (255, 255, 255))
                #pygame.draw.line(screen, (255, 255, 255), (75, 520+35*count-2), (600, 520+35*count-2))

    if Time.getWeekday()=='星期六' or Time.getWeekday()=='星期日' or count==0 :
        ClassFont.render_to(screen,(75,200),"今日无课程",(30,144,255))
    #pygame.draw.line(screen,(255,255,255),(75,518),(75,520+35*count-2))
    #pygame.draw.line(screen, (255, 255, 255), (600, 518), (600, 520 + 35 * count - 2))
    pygame.draw.rect(screen,(255,255,255),(70,518,530,35*count),2,border_radius=10)

    Tomorrowcount = 0
    if Time.getWeekday()!='星期六' and Time.getWeekday()!='星期五':
        ClassFont.render_to(screen,(75,550+35+35*count),"明日课程:",(30,144,255))
        Tomorrow=Time.list[(Time.getWday()+1)%7]

        for i in range(1,6):
            if Class.getClass(i,Tomorrow)['course']!='无课程':
                ClassInfo=Class.getClass(i,Tomorrow)
                ClassFont.render_to(screen,(75,550+35+35*count+35*(Tomorrowcount+1)),'第'+str(i)+'节:'+ClassInfo['course'],(255-random.randint(0,128),255-random.randint(0,128),255-random.randint(0,128)))
                Tomorrowcount+=1
    if Time.getWeekday()=='星期六' or Time.getWeekday()=='星期五' or Tomorrowcount==0:
        ClassFont.render_to(screen, (75, 550+35*count), "明日无课程", (30, 144, 255))

def showHot():#百度热搜以及知乎专栏
    NameFont=pygame.freetype.Font("FontLib/setup/苹方黑体-中粗-简.ttf",36)
    NameFont.render_to(screen,(50,1450+225),'实时热点',(255,255,255))
    HotFont=pygame.freetype.Font("FontLib/setup/苹方黑体-准-简.ttf",24)
    for i in range(3):
        HotFont.render_to(screen,(50,225+1500+i*25),Hot[i],(255,255,255))
    pygame.draw.line(screen,(255,255,255),(50,1590),(520,1590))#分隔线
    QRPic=pygame.image.load("QR/QR.png")
    QRPic=pygame.transform.scale(QRPic,(225,225))
    QRPicRect=QRPic.get_rect()
    QRPicRect.center=(900,1700)
    screen.blit(QRPic,QRPicRect)
    NameFont.render_to(screen,(50,225+1600),"知乎日报："+'『'+ZhuanLanTitle+'』',(255,255,255))
    HotFont.render_to(screen,(810,1680-130),"扫描以阅读日报",(255,255,255))

def showHistory():
    NameFont=pygame.freetype.Font("FontLib/setup/楷体.TTF",42)
    NameFont.render_to(screen,(50,1450),"『史·鉴』",(255,255,255))
    ContentFont=pygame.freetype.Font("FontLib/setup/楷体.TTF",30)
    ContentFont.render_to(screen,(50,1500),HistoryMessage,(255,255,255))

def showVer():
    VerFont=pygame.freetype.Font("FontLib/setup/苹方黑体-细-简.ttf",10)
    VerFont.render_to(screen,(790,1900),'Magirror '+ver+' @Pixel·Chen ®All Rights Reserved',(255,255,255))

def showSentence():
    SentenceFont=pygame.freetype.Font("FontLib/setup/楷体.TTF",36)
    length=len(DailySentence)
    SentenceFont.render_to(screen,(540-36*length/2,1200),DailySentence,(255,255,255))
    #screen.blit(SentenceRect,[540,960])
updateAPI()

screen.blit(WallPaper,(0,0))
showTime()
showMainWeather()
showMoreWeather()
showHot()
showVer()
showClass()
showHistory()
showSentence()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    #screen.blit(WallPaper,dest=(0,0,580,450),area=(0,0,580,450))#需要实时刷新的其实就只有时间
    if Time.getMinute()==30 and Time.getSec()==0:#整点更新API数据
        updateAPI()
        screen.blit(WallPaper,(0,0))
        showMainWeather()
        showMoreWeather()
        showHot()
        showVer()
        showClass()
        showHistory()
        showSentence()
    screen.blit(CutPaper,(0,0))
    showTime()

    clock.tick(FPS)
    pygame.display.update()
