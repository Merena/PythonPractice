import scrapy
from scrapy.http import Request
from myscrapy.items import AnjukeHouseItem
from urllib.parse import urlparse
import re
import logging

loggerDataName = 'anjuke'
log_dataInfo_path = 'logs/anjuke.log'
# log = Log

repos = []
class AnjukeSpider(scrapy.Spider):

    name = "AnjukeSpider"
    allowed_domains = ['anjuke.com']
    start_urls = ['https://guangzhou.anjuke.com/sale/']
    headers = {
        "HOST": "guangzhou.anjuke.com",
        "Referer": "https://guangzhou.anjuke.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def parse(self, response):
        ret_list = response.css('#houselist-mod-new > li')
        for item in ret_list:
            house_item = AnjukeHouseItem()
            house_item['img_url'] = item.css('img::attr("src")').get()
            house_item['title'] = item.css('a::attr("title")').get()
            house_item['detail_href'] = item.css('a::attr("href")').get()
            house_item['addr'] = item.css('span.comm-address::attr("title")').get()
            house_item['good'] = item.css('span.item-tags.tag-others::text').getall()
            house_item['size'] = item.css('div.house-details > div:nth-child(2) > span::text').getall()
            house_item['price'] = item.css('span.unit-price::text').get()


            yield Request(url=house_item['detail_href'], meta={"refer_url": response.url},
                          callback=self.parse_detail, headers=self.headers)
            yield house_item

        next_url = response.css('a.aNxt::attr("href")').get()
        print(next_url)

        if next_url is not None:
            yield Request(url=next_url, meta={"refer_url": response.url},
                          callback=self.parse, headers=self.headers)


    def parse_detail(self, response):

        pass