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
            'Cookie': '_octo=GH1.1.1290119782.1559474823; _ga=GA1.2.71546662.1559474842; _device_id=b696399a06253b1b8195ecd257dad20c; logged_in=no; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; _gh_sess=aEFzQXV2eXpUeFRsTGZMUVFaRllxMEhOQkl3MlE4cnIyOVYzRVVPVGdZU09Sb2tmOTg0WDVEV0JDQXVrU1FGdng3eE5UajJ5MGR1Zy9JTWRWN1pDcmU0VEcvNXllaUhLVEt4UjRiV2YxMVBKbjB5alhoYU83Y3lUOHZKYzlmTFJ6cm5TdWJoczdNb21JeHZXUThZbnowTlRlZUc2Vk1hQVZ4V1RiSXpQa2FsZVhsWUlobzlSbHdYelJnNW5SelVDOVVMdFBLZVZ0czlrZFU4U2I1NHJNTW5DSGlBL2dRMFMvRDgzWVVmNkd1d1Q1MlY3WVNnTDU1eDJLdXNiMk5ZckFZVm9CSHUxUTgva0hwKzBVMUF5WDh0RFNwLzhGWUx3b25zQTZDN2VmcUxOMTY3Y0NVNlpZSVNQQlhtVmlyeUtVWE02WG9lcGI2UHo3RTJ3a0RkdU5qaUlyb1JIOXVnSVdoYTdKSFYrbVZLazg3YjV3ZjlkZ043WE91WExuaFplQ0FER1hCZDBFTXl0c3ZDbFR0VUVuUT09LS1xSDgzeURmclhBeFNKcDlOOW5tR1FRPT0%3D--8b8a623185b4c1e1151c4ba3a1ebbc3e726842c4',
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }

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