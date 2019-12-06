import scrapy
import re

class Spider(scrapy.Spider):
    name = 'TextPrxoy'
    allowed_domains = []

    def start_requests(self):
        url = 'https://ip.cn'

        for i in range(15):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        content = response.text
        ip = re.search('您现在的 IP：<code>(.*?)</code></p>', content)

        if ip is not None:
            print('您的IP:', ip.group(1))
        else:
            print('未查到您的IP')
