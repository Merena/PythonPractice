import requests
import lxml.html
import textwrap
import struct

def getWeatherReport(url):
    respond = requests.get(url)
    respond.encoding = respond.apparent_encoding

    # print(respond.text)
    selector = lxml.html.fromstring(respond.text)
    dates = selector.xpath('//div[@id="content"]/table[@class="b"]/tr')

    a = dates[0].xpath('//td[2]/b/a/text()')
    # cities = dates[0].xpath('//td[1]/b/text()')
    yu = dates[0].xpath('//td[3]/text()')
    feng = dates[0].xpath('//td[4]/text()')
    wendu = dates[0].xpath('//td[5]/text()')
    night_yu = dates[0].xpath('//td[5]/text()')
    night_feng = dates[0].xpath('//td[6]/text()')
    night_wendu = dates[0].xpath('//td[7]/text()')

    # yu = [textwrap.dedent(x) for x in yu]
    yu = [x.split()[0] for x in yu]
    #print(a,cities, yu, feng, wendu, night_yu, night_feng, night_wendu)

    c = zip(a,yu, feng, wendu, night_yu, night_feng, night_wendu)

    for i in c:
        print(i)
    print(c)

    textwrap.TextWrapper.tabsize()

if __name__ == '__main__':
    getWeatherReport('http://www.tianqihoubao.com/weather/top/guangzhou.html')