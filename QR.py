from MyQR import myqr
from skimage import io
import requests
import random


def getQR():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        SourceURL = "http://news-at.zhihu.com/api/4/news/latest"

        Content = requests.get(SourceURL, headers=headers, timeout=2)
        Content = eval(Content.text)
        ContentList = Content['stories']
        length = len(ContentList)
        chosenIndex = random.randint(0, length - 1)
        chosenContent = ContentList[chosenIndex]
        title = chosenContent['title']
        picURL = chosenContent['images'][0]
        newPicURL = picURL.replace('\\', '')  # python自动对/进行了转义\/，但我们不需要他这么自作多情的转义，所以我们要把\删掉
        contentURL = chosenContent['url']
        newContentURL = contentURL.replace('\\', '')
        date = Content['date']
        pic = io.imread(newPicURL)
        io.imsave("QR/BackGround.jpg", pic)
        version, level, qr_name = myqr.run(
            newContentURL,
            picture="QR/BackGround.jpg",
            colorized=True,
            save_name='QR.png',
            save_dir='QR/'

        )
        print("QR refreshed successfully.")
        return title, date
    except:
        return "0.O参数错误","Wrong"
