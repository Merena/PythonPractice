import scrapy
import json

class GithubSpider(scrapy.Spider):
    name = "GithubSpider"
    allowed_domains = ['github.com']
    start_urls = ['https://api.github.com/search/repositories?q=%E7%88%AC%E8%99%AB%20java']

    headers = {
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
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    def start_requests(self):
        func = self.parse_resultcnt
        urls = self.gen_urls()

        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=func)

    def gen_urls(self, start=1, stop=2):
        urls = ['https://github.com/search?l=&p={p}&q=swift+extension%3Acodesnippet&type=Code'.format(p=p) for p in
                range(start, stop)]
        return urls

    def parse_resultcnt(self, response):
        """ 解析特定查询下返回的结果数 """
        datas = json.loads(response.body.decode("utf-8"))
        # items = datas['items']
        # print(len(items))
        #
        # reps = []
        # for item in items:
        #     rep = MygithubItem()
        #     owner = item['owner']
        #     rep['id'] = item['id']
        #     rep['author'] = item['full_name']
        #     rep['desc'] = item['description']
        #     rep['link'] = item['html_url']
        #     rep['avatar'] = owner.get('avatar_url')
        #     rep['posttime'] = item['pushed_at']
        #     rep['language'] = item['language']
        #     reps.append(rep)
        #     yield rep

        # print(reps)

    # def parse(self, response):


    # def parse_repo(self, response):
    #     self.repo_cnt += 1
    #     name = response.xpath('//strong[@itemprop="name"]//text()').extract_first()
    #     git_url = response.xpath('//clipboard-copy/@value').extract_first()
    #
    #     self.logger.info(git_url)
