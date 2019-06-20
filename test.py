import requests
import lxml.html


def getContentOfUrl(url):
    tmp = requests.get(realUrl)
    html = tmp.content.decode('utf-8')

    selector = lxml.html.fromstring(html)
    aa = selector.xpath('//*[@id="readArea"]/div[1]/div[2]/p')

    content = ''
    for element in aa:
        if element.text != None :
            content += element.text + '\r\n\r\n'

    return content


tmp = requests.get('https://www.17k.com/list/2931226.html')
html = tmp.content.decode('utf-8')

selector = lxml.html.fromstring(html)
aa = selector.xpath('/html/body/div[5]/dl/dd/a/@href')

file = open('text.txt', 'w+')


for i, each in enumerate(aa):

    if i > 20:
        break

    realUrl = 'https://www.17k.com%s' % each

    text = getContentOfUrl(realUrl)
    ret = file.write(text)
    print(text)

file.close()

