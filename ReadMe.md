[TOC]



# Magirror——基于pygame的树莓派魔镜

版本v1.2.0(不定期更新版本)

## （一）功能概览

![UI2.0](C:\Users\chen\source\repos\Magirror(Github开源）\UI2.0.png)

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

pygame 2.0.1    ( 通过pip 安装)

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

#### 修改Weather.py

![WeatherAPI](C:\Users\chen\source\repos\Magirror(Github开源）\WeatherAPI.jpg)

将第五行的API秘钥修改为你自己的

#### 修改Fun.py

![FunAPI](C:\Users\chen\source\repos\Magirror(Github开源）\FunAPI.jpg)

将对应的秘钥修改为你自己的

### 2.自定义数据

#### 写入自己的课表信息

![SetClassTable](C:\Users\chen\source\repos\Magirror(Github开源）\SetClassTable.jpg)

table是一个字典，字典第一层的键为星期，第二层的键为课序号。第三层的键为课程名course,周次range,上课地点room.

![MyClass](C:\Users\chen\source\repos\Magirror(Github开源）\MyClass.png)

比如上图是我的课表，那么对应的table结构就是第一张图。可以根据自己实际情况修改table（对于没有python基础的同学来说可能有点难，如果自己不会改可以联系我QQ:1640867082)

#### 自定义一言句子类型

一言提供的句子类型总共有12种（不过貌似第12种抖机灵类无法使用），可以根据自己喜好或者送礼对象（恩很多人魔镜做出来是送给女孩子的）增加或删除句子类型。

具体操作为：

![image-20210411113127160](C:\Users\chen\AppData\Roaming\Typora\typora-user-images\image-20210411113127160.png)

在16行的中括号内增加或删除类型（字母'a'~'k'的代号）即可。代号代表的类型参见 [链接](https://pa-1251215871.cos-website.ap-chengdu.myqcloud.com/sentence/#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

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

## （六）常见问题

有问题欢迎随时联系QQ 1640867082

我炒鸡热心的！

## （柒）所以可以捐赠鼓励一下吗？

![image-20210411115830784](C:\Users\chen\AppData\Roaming\Typora\typora-user-images\image-20210411115830784.png)