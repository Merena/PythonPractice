import requests
import lxml
import re
from urllib.request import urlretrieve


def get_img():
    url = 'http://www.uustv.com/'

    data = {
        'word': '姓名',
        'sizes': 60,
        'fonts': 'jfcs.ttf',
        'fontcolor': '#000000'}
    result = requests.post(url, data).content.decode()
    # result = requests.get(url)
    # # result.encoding = 'utf-8'
    # result.encoding = result.apparent_encoding
    # http://www.uustv.com/tmp/156094850779558.gif

    tt = re.findall('<div class="tu">﻿<img src="(.*?)"/></div>', result)
    imgUrl = url + tt[0]
    img_file = r'./img.gif'
    urlretrieve(imgUrl, img_file)
    print(result)


if __name__ == '__main__':
    get_img()