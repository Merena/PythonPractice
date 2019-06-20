#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import re
import lxml.html


def getBookChapterUrls(selector):
    info = selector.xpath('/html/body/div[@class="Main List"]/dl[@class="Volume"]/dd/a')
    item_list = []
    for each in info:
        aa = each.xpath('@href')[0]
        bb = each.xpath('span/text()')[0]

        url = 'https://www.17k.com%s' % aa
        item_list.append((bb.strip(), url))

    return item_list

def getContentOfChapterUrl(contentUrl):
    test = requests.get(contentUrl)
    html = test.content.decode('utf-8')

    selector = lxml.html.fromstring(html)
    tmp = selector.xpath('//*[@id="readArea"]/div[@class="readAreaBox content"]/div[@class="p"]/p')

    content = ''
    for each in tmp:
        classAttr = each.xpath('@class')

        # if each.text and each.text.startswith('本书首发来自'):
        #     print(each.text)

        if len(classAttr)>0 and classAttr[0]=='copy':
            continue

        if each.text:
            content += '  '+ each.text+'\r\n\r\n'

    return content


def downloadBookOfUrl(bookUrl):

    test = requests.get(bookUrl)
    html = test.content.decode('utf-8')
    selector = lxml.html.fromstring(html)
    tmpUrl = selector.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/dl/dt/a/@href")[0]
    tableOfContentsUrl = 'https://www.17k.com%s' % tmpUrl

    test = requests.get(tableOfContentsUrl)
    html = test.content.decode('utf-8')
    selector = lxml.html.fromstring(html)
    title = selector.xpath('/html/body/div[@class="Main List"]/h1[@class="Title"]/text()')[0]

    print(title, '开始下载', tableOfContentsUrl)

    urlList = getBookChapterUrls(selector)

    file = open('%s.txt' % title, 'w+')
    for i, element in enumerate(urlList):
        b = getContentOfChapterUrl(element[1])
        file.write(b)

        print('章节', i, '下载完成')

        if i > 10:
            break

    file.close()
    print(title, '下载完成')

def downloadFromPages(pageUrls):
    for eachPageUrl in pageUrls:
        test = requests.get(eachPageUrl)
        html = test.content.decode('utf-8')
        selector = lxml.html.fromstring(html)
        bookUrls = selector.xpath("/html/body/div[4]/div[3]/div[2]/table/tbody/tr/td[3]/span/a/@href")

        for eachBookUrl in bookUrls:
            downloadBookOfUrl('https:%s' % eachBookUrl)


test = requests.get('https://www.17k.com/all/book/2_0_0_0_0_7_1_0_1.html')
html = test.content.decode('utf-8')
selector = lxml.html.fromstring(html)
allPages = selector.xpath('/html/body/div[@class="main searchjg"]/div[@class="search-list"]/div[@class="page"]/text()')[7];

pageNo = allPages.strip()
pageNo = pageNo.strip(r' 共页')

pageUrls = []
for i in range(0, int(pageNo)) :
    tmp = 'https://www.17k.com/all/book/2_0_0_0_0_7_1_0_1.html'
    pattern = re.compile(r'(\d+)\.html')

    out = re.sub(pattern, '%d.html'%(i+1), tmp)

    pageUrls.append(out)

# print(pageUrls)
downloadFromPages(pageUrls)

