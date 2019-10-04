import requests
import parsel

# re正则
# print(sel.re('正则匹配格式'))

# xpath
# print(sel.xpath('xpath').getall()) #getall获取所有

# css选择器
# print(sel.css('css选择器 ::text').extract_first())#获取第一个

'''
xpath取到节点后，取文本用/text() 取属性值用 @ ，如value1 = html.xpath('//a/@href')
'''
a = requests.get('https://www.sohu.com/a/226519274_465944')
a.encoding = a.apparent_encoding
content = a.text

sel = parsel.Selector(content)
b = sel.xpath('//*[@id="article-container"]/div[2]/div[1]/div[1]/div[1]/h1/text()').getall()
# print(content)
b = [x.strip() for x in b if not x.isspace()]
print(b)
