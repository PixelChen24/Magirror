@[toc]
# Magirror——基于pygame的树莓派魔镜
原创项目，求Star！



**首先，为什么要用pygame？**

——GitHub上已经有一个MagicMirror的项目了，star数也很高。我去试着装了一下，无奈环境配了好几天都没弄好，毕竟作者是外国人，网络情况什么的（你懂得）和国内不大一样，又是装nodejs又是装electron，各种坑。于是我就萌发了用pygame来写一个魔镜的想法，只要你的设备支持完整的python（不包括MicroPython）就能运行！真的是有手就行！

把这个镜子完整的做出来，送给女生真的是很好康的桌面摆件呢



版本v1.2.2(不定期更新版本)

## （一）功能概览

![整体UI](https://img-blog.csdnimg.cn/20210412104155609.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDgzODU3,size_16,color_FFFFFF,t_70#pic_center)
![实地拍摄](/Assets/RealTime.jpg)
目前把软件部分写好了，原子镜还没上，包装也没开始做。不过这些应该都是小事，而且我还想扩展一些智能家居，传感器，语音助手之类的IO设备功能，于是就没有做包装。

1. 显示天气，生活指数

2. 显示今明两天课表信息

3. 显示当日热点

4. 推送高质量知乎日报，可以扫描QR码阅读

5. 历史上的今天

6. 一段让人心动的句子

   **以上数据除时间实时刷新外，每到整点刷新一次**

7. 基于blinker的智能家居控制（开发中）

8. 语音聊天机器人（开发中）

## （二）环境要求

### 1.硬件要求

1.装好官方raspbian系统的树莓派

2.一块1080p的小屏幕 [推荐淘宝链接](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.3e352e8dEUsahj&id=558956849119&_u=b2029g7480bb2d)

3.单向透光原子镜(魔镜的灵魂！没了这块镜子你的魔镜只能是一块屏幕) [推荐淘宝链接](https://item.taobao.com/item.htm?spm=a230r.1.14.21.37671f49BXbKpo&id=555111074798&ns=1&abbucket=17#detail)

### 2.基础软件要求

python3

pygame 1.9.6    ( 通过pip 安装)

### 3.pip包

requests

pillow

MyQR

skimage

### 4.HTTPS API接口

#### [聚合数据(需要注册账号)](https://www.juhe.cn/)

聚合数据是一个比较良心的API平台，对于免费用户每天有100次免费调用。使用此平台*需要注册账号并实名认证*。

1.[聚合数据 历史上的今天](https://www.juhe.cn/docs/api/id/63)

2.[聚合数据 万年历](https://www.juhe.cn/docs/api/id/177)

3.[聚合数据 新闻头条](https://www.juhe.cn/docs/api/id/235) （可选，新闻质量不太好，类似UC风格标题）

#### [心知天气(需要注册账号)](https://www.seniverse.com/)

心知天气为开发者提供天气方面接口调用的服务。免费用户调用次数无限，但有20QPS并发限制（显然个人使用的话远远不会有那么高的QPS，所以这项限制对个人来说等于没有）。*需要创建账户免费申请。*[产品文档](https://docs.seniverse.com/api/weather/now.html)

1.[心知天气 实时天气](https://www.seniverse.com/products?iid=new)

2.[心知天气 未来几日天气预报](https://www.seniverse.com/products?iid=new)

3.[心知天气 生活指数](https://www.seniverse.com/products?iid=new)

以上三个接口只需要免费开通服务即可全部获得，由同一个API秘钥管理。

#### [知乎日报](http://news-at.zhihu.com/api/4/news/latest)

知乎日报没有官方给出的API，此处请求地址实质上是网上某大佬自己制作的接口。

#### [百度热搜](http://top.baidu.com/mobile_v2/buzz/hotspot/)

百度头条没有官方给出的API，此处请求地址实质上是网上某大佬自己制作的接口。

#### [一言](https://hitokoto.cn/)

一言为开发者提供数据接口，获取一句打动灵魂的句子。

## （三）环境配置

### 1.配置API秘钥相关信息

#### 修改Function/Weather.py

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210412105220235.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDgzODU3,size_16,color_FFFFFF,t_70#pic_center)


将第五行的API秘钥修改为你自己的

#### 修改Function/Fun.py

![将对应的秘钥修改为你自己的](https://img-blog.csdnimg.cn/20210412105249753.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDgzODU3,size_16,color_FFFFFF,t_70#pic_center)
将对应的秘钥修改为你自己的



### 2.自定义数据

#### 写入自己的课表信息

![在这里插入图片描述](https://img-blog.csdnimg.cn/202104121053325.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDgzODU3,size_16,color_FFFFFF,t_70#pic_center)


table是一个字典，字典第一层的键为星期，第二层的键为课序号。第三层的键为课程名course,周次range,上课地点room.

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021041210534665.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDgzODU3,size_16,color_FFFFFF,t_70#pic_center)


比如上图是我的课表，那么对应的table结构就是第一张图。可以根据自己实际情况修改table（对于没有python基础的同学来说可能有点难，如果自己不会改可以联系我QQ:1640867082)

#### 自定义一言句子类型

一言提供的句子类型总共有12种（不过貌似第12种抖机灵类无法使用），可以根据自己喜好或者送礼对象（恩很多人魔镜做出来是送给女孩子的）增加或删除句子类型。

具体操作为：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210412105407209.jpg#pic_center)


Function/Fun.py文件，在16行的中括号内增加或删除类型（字母'a'~'k'的代号）即可。代号代表的类型参见 [链接](https://pa-1251215871.cos-website.ap-chengdu.myqcloud.com/sentence/#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

### 3.树莓派换python3

树莓派默认使用python2.7，然而本人在Windows上面开发好之后放上去运行报了一堆奇怪的错误，罪魁祸首是python2.7

因此最好将默认python版本换为python3 [详见教程](https://blog.csdn.net/ylzmm/article/details/107827065)

## （四）运行

**运行之前还有最后一件事，把树莓派的显示器旋转90度！因为默认显示器是横向的，但我们的镜子是纵向1080*1920的，因此需要旋转屏幕。**

[旋转屏幕教程](https://www.jianshu.com/p/657f6e113666)

恭喜！现在终于可以愉快的运行魔镜了！

在终端运行

```shell
python main.py
```

即可

你也可以编写一个shell脚本，使树莓派开机就自动运行此命令。

## （五）组装

软件都写好了，硬件连线也就电源线和HDMI显示线，(相信聪明的你会自己做外观了吧

（其实是我自己还没有把这些东西装起来，教程还不能图文并茂的写，以后会补起来的）

树莓派的电源线可以和显示器的电源线公用一根，通过改装USB先把两根焊成一根。

如果纠结USB或者HDMI线太硬不好控制边框空间的话，可以尝试淘宝搜一下“直角USB”或者“直角HDMI”之类的，你会眼前一亮的



电源线公用一根，通过改装USB先把两根焊成一根。

如果纠结USB或者HDMI线太硬不好控制边框空间的话，可以尝试淘宝搜一下“直角USB”或者“直角HDMI”之类的，你会眼前一亮的

## （六）常见问题
1.如果你是先在Windows上面调试的，发现屏幕显示不完整，那么请你查看一下你的屏幕有没有设置缩放。我就是最开始默认开了125%的缩放结果坐标位置老是找不对。

2.目前心知天气免费用户仅支持国内天气查询，所以如果你是在国外或者是电脑挂着梯子的话，获取天气是会出错的，具体表现为数据显示为“x"

3.在Windows运行和树莓派运行效果可能有一点点不一样。树莓派默认pygame版本为1.9.4，所以运行可能会报错：

![SDL错误](https://magirror.oss-cn-beijing.aliyuncs.com/Errors/libsdl%E6%8A%A5%E9%94%99.png)

这时你需要安装libSDL,在树莓派终端通过命令行安装：

``` shell
sudo apt install libsdl2-ttf-2.0-0
```


有其他问题欢迎随时联系QQ 1640867082

我炒鸡热心的！

## （柒）所以可以捐赠鼓励一下吗？
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210412105531172.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDgzODU3,size_16,color_FFFFFF,t_70#pic_center)

