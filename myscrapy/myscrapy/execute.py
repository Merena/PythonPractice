#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute('scrapy crawl GithubSpider'.split())
# cmdline.execute('scrapy crawl blogspider'.split())