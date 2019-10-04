import scrapy
import json
from myscrapy.items import RepoItem

repos = []
class GithubSpider(scrapy.Spider):

    name = "GithubSpider2"
    allowed_domains = ['github.com']


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_octo=GH1.1.1290119782.1559474823; _ga=GA1.2.71546662.1559474842; _device_id=b696399a06253b1b8195ecd257dad20c; tz=Asia%2FShanghai; user_session=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; __Host-user_session_same_site=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; logged_in=yes; dotcom_user=Merena; has_recent_activity=1; _gat=1; _gh_sess=SjJvamlXbjhmdlYxRmorYkNPeGJkdGI1c0VOQWVDa083bUxWdWkvVmcvWnNTVnVlK01tRXZDck56d0FpWno1SDNQZ21mNmZ5RVlHTzQxREVac1BSd0hRRkoxclJjelIvSHFteHFDVFdqVnJwUlhZeE9DVXZWblVoWitqV0I0bmF3WEFMOVVSOFZkZ0o4MXVKT2VTeDFzN0tLMFFncStkTDhFbXpZRmVVL2JsaXhnR0hYM2RJeXkxVFhZTGVxWXp1SzU3NGJScTV1aDhYZUtNNllpMmZyZ1lxWCt1TExkVWo3dFdSNEZYVTVUbz0tLXVFUjNneWlyYVVYaVo0TjZUbmV4Z2c9PQ%3D%3D--a78c7b3ae4f1f7ee1526e0aafa94c585313eda44',
        'Host': 'github.com',
        'If-None-Match': 'W/"23a8ee73eea45224f3be70d1a2b0083b"',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    def start_requests(self):
        func = self.parse_resultcnt
        urls = self.gen_urls()

        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=func)

    def gen_urls(self, start=1, stop=2):
        urls = ['https://github.com/search?l=Python&o=desc&p={p}&q=start_requests&s=indexed&type=Code'.format(p=p) for p in
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
