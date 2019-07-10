import requests
import lxml.html
import re
from urllib.request import urlretrieve
import os
import urllib
from multiprocessing import Pool

class GithubSpider(object):

    def __init__(self):
        self.urls = set()
        self.HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.1861646046.1562724004; _octo=GH1.1.156582776.1562724004; tz=Asia%2FShanghai; _device_id=0d3305d2f82236d33a5f00217e3fbb59; user_session=uAmp-876pLtdE5MFw9eiB6WKY9voTeseVXtKWY-X6VmwKMul; __Host-user_session_same_site=uAmp-876pLtdE5MFw9eiB6WKY9voTeseVXtKWY-X6VmwKMul; logged_in=yes; dotcom_user=Merena; has_recent_activity=1; _gh_sess=THVsSmFRaUR5U092Tzh5M09tMzMrTWhvWlFpcThVM3g2UWhTRElIT0ZXTm0raUhwUXB4eTAwMm1pV0xSY05wYnY4T2NvQUt6SVlUY25tL0FmQUJPMlhiUk1vU0xJWjNzTDZOWG83WHlIUSsrWTNOS2RFai9NSHk2T3NmL09PbjJaRFBzNzFteGZqOTdnRmt2Lzg2bHM1TmxUL0NJSXphRTd3UW8rUEVtdksvZnZHUU9KMVczTUtyMVY5clR2VzNMWElNM2U4UFJMOFNqWUhFYVNKcGJVYy9vSVFaOWNwOWtjdDRGQ0c3N3ZHNXZpYmhJYXEwdEE2RDkvVVBxbDl6VTlMcG53ajFGT2xpR3o5U1djSjQyYzVRM1hBM29LVERpTndNWGtmM2N5YmNpWFgvMGx0aTl5RUxBNkJodXM0cVloNmJ2YW5nNUl5emxKQkRyT3ljcGxBPT0tLXFCQ2lDOUFHUzBNQ3VaUERna0FjUmc9PQ%3D%3D--d722a329883d808c70c50612219d4837bcd2bb13; _gat=1',
            'Host': 'github.com',
            'If-None-Match': 'W/"15f6369b033f37964cbe99bd85d1fdff"',
            'Referer': 'https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsearch%3Fl%3D%26p%3D1%26q%3Dswift%2Bextension%253Acodesnippet%26type%3DCode',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'    }

    def getContentOfUrl(self, url):
        # url = 'https://github.com/trending/{language}'.format(language='python')
        respond = requests.get(url, headers=self.HEADERS)
        respond.encoding = respond.apparent_encoding
        selector = lxml.html.fromstring(respond.text)
        # print(respond.text)

        tmp = selector.xpath("//div[@class='code-list-item col-12 py-4 code-list-item-public ']/div[1]/div/a[2]/@href")
        urls = ["https://github.com"+x.replace(r'/blob/', r'/raw/') for x in tmp]
        print(urls)

        self.create_dir("codesnippets")

        for url in urls:
            self.urls.add(url)

            # file_name = url.split(r'/')[-1]
            #
            # respond = requests.get(url)
            # respond.encoding = respond.apparent_encoding
            #
            # urlretrieve(url, os.path.join("codesnippets", file_name))
        print(urls)

    def create_dir(self, name):
        if not os.path.exists(name):
            os.makedirs(name)

    def gen_urls(self, start=1, stop=10):
        urls = ['https://github.com/search?l=&p={p}&q=swift+extension%3Acodesnippet&type=Code'.format(p=p) for p in range(start, stop)]
        return urls

    def scrapy(self):
        # urls = self.gen_urls(1, 100)
        #
        # for url in urls:
        #     self.getContentOfUrl(url)

        self.create_dir("codesnippets")
        with open(os.path.join("codesnippets", 'allUrls.txt'), 'r', newline='\r\n') as f:
            self.urls = [x.strip() for x in f.readlines()]

        for url in self.urls:
            file_name = os.path.join("codesnippets", url.split(r'/')[-1])
            if not os.path.exists(file_name):
                respond = requests.get(url)
                respond.encoding = respond.apparent_encoding

                urlretrieve(url, file_name)

if __name__ == '__main__':
    GithubSpider().scrapy()