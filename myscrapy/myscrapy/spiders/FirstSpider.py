'''
--------《Python从菜鸟到高手》源代码------------

欧瑞科技版权所有
作者：李宁
如有任何技术问题，请加QQ技术讨论群：264268059    
或关注“极客起源”订阅号或“欧瑞科技”服务号或扫码关注订阅号和服务号，二维码在源代码根目录
如果QQ群已满，请访问https://geekori.com，在右侧查看最新的QQ群，同时可以扫码关注公众号

“欧瑞学院”是欧瑞科技旗下在线IT教育学院，包含大量IT前沿视频课程，
请访问http://geekori.com/edu或关注前面提到的订阅号和服务号，进入移动版的欧瑞学院

“极客题库”是欧瑞科技旗下在线题库，请扫描源代码根目录中的小程序码安装“极客题库”小程序

关于更多信息，请访问下面的页面
https://geekori.com/help/videocourse/readme.html



'''
import scrapy
from bs4 import *
from myscrapy.items import CourseItem

class BlogSpider(scrapy.Spider):


    name = 'blogspider'
    # 设定域名
    allowed_domains = ["imooc.com"]
    # 填写爬取地址
    start_urls = ["http://www.imooc.com/course/list"]

    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = CourseItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('div.moco-course-list'):
            # 获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            # 获取div中的课程标题
            item['title'] = box.xpath('.//h3[@class="course-card-name"]/text()').extract()[0].strip()
            # 获取div中的标题图片地址
            item['image_url'] = 'http:' + box.xpath('.//@src').extract()[0]
            # 获取div中的学生人数
            item['student'] = box.xpath('.//span/text()').extract()[1].strip()
            # 获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            # 返回信息
            yield item