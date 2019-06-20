#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys, json

if __name__ == '__main__':
     target = 'http://unsplash.com/napi/feeds/home'
     headers = {'authorization':'your Client-ID'}
     req = requests.get(url=target, headers=headers, verify=False)
     html = json.loads(req.text)
     next_page = html['next_page']
     print('下一页地址:',next_page)
     for each in html['photos']:
          print('图片ID:',each['id'])