import scrapy
import json
from myscrapy.items import RepoItem

repos = []


class GithubSpider2(scrapy.Spider):
    name = "GithubSpider2"
    allowed_domains = ['github.com']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_octo=GH1.1.1290119782.1559474823; _ga=GA1.2.71546662.1559474842; _device_id=b696399a06253b1b8195ecd257dad20c; tz=Asia%2FShanghai; user_session=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; __Host-user_session_same_site=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; logged_in=yes; dotcom_user=Merena; has_recent_activity=1; _gat=1; _gh_sess=VGc1ekVkODBJNHp1b2xoc1JaWXlHNmhLL2dDa1JvNXYrc2RLdDNSZ0wxYUlGQU9jeklLOUFxLzdad2phUGhPbkhWSU5SaUphdnBwYVJjWnNET0ZUcHJXSTB5N29BcEY4aHpPNmhqNjd6Z0xIeXIzZVNpd3pzTEw1VmdpTVl1ejRsNll2THhlNjF6dUZMbnF3dmJQL2FtNFhFY09rY0tiajIrZHErbHU1eGd0QnN3eE9TTmtHUWVhdG8zdXNZYnhjWmwwWGxBRUptai9aQlJ6OHhmMjM3dFFPK0F1YksrRExzdkFYc2NFckZ5UnhudnpiQmJMcGlVeEZWV3ltaEdiQ01RT3BvOXc1a0VOYkhHdHRRcEd3SENBSlBXVVR4UEdnZ2h1OEMzcFoxaWx4dWNuRGx1a0VFcXBqcERQQVdPNzUtLTc3bnV5NjRmdm1McGdUWmpzbFVnSUE9PQ%3D%3D--836221a078de8cb9f19fe4d5ac3f25d35d01f439',
        'Host': 'github.com',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    def start_requests(self):
        func = self.parse_resultcnt
        urls = self.gen_urls()

        for url in urls:
            yield scrapy.Request(url=url,  callback=func)

    def gen_urls(self, start=1, stop=2):
        urls = ['https://github.com/search?l=Python&o=desc&p={p}&q=start_requests&s=indexed&type=Code'.format(p=p) for p
                in
                range(start, stop)]
        return urls

    def parse_resultcnt(self, response):

        a = response.xpath('//*[@id="code_search_results"]/div[1]/div[1]/div/div[2]/a/@data-hydro-click')

        for i in a:
            repo_info = i.xpath('.//@data-hydro-click').get()
            time_str = i.xpath('.//relative-time/@datetime').get()
            stars = i.xpath('.//a[@class="muted-link"]/text()').getall()
            stars = [x.strip() for x in stars if not x.isspace()][0]

            dic = json.loads(repo_info)
            url = dic['payload']['result']['url']

            repo = RepoItem()
            repo['url'] = url
            repo['update_time'] = time_str
            repo['stars'] = stars

            repos.append(repo)

        print(repos)
        # b = response.selector
        """ 解析特定查询下返回的结果数 """
        # datas = json.loads(response.text)
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
