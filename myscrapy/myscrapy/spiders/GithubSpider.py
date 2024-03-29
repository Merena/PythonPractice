import scrapy
import json
from myscrapy.items import RepoItem

repos = []
class GithubSpider(scrapy.Spider):

    name = "GithubSpider"
    allowed_domains = ['github.com']


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': '_octo=GH1.1.1290119782.1559474823; _ga=GA1.2.71546662.1559474842; _device_id=b696399a06253b1b8195ecd257dad20c; logged_in=no; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=cHRtOHlJdFVsSEc4cE1xTmk4TWw1MlJnU2VCMWpYVUxTZnlveDMvM2tySHZsV3ZUYklVQlVmcmZFSkFpa1JOTTV2RC9hUzF6QmgzUEJDU2F1bVFDR2x6VzZCbHVwbWc4Um02STBPSWI3QlczV2tJaW1ZSzErQ0lrUGdxMlV1SHl3dGs1bkQyU092OEJJM2tzR09pKzN6RFpJNkUwaUtSdGJtS3k0cXMwWE5WeDFlM25Da1NyT0w5ZWptcnJIMC9FNEZ2amJnbWkwWGZhQnBEOFFYV2p2WGplWCtzTi9Ha3RsNHI0R3I1V1YyWHJpbjhsbWdqN1pNS0tNRk9aemtVTXBMS0lKOEM0alVMenk3ZlJNT1Z1OGUxQmxBa2hnd2ZDbWM2dktyM0VhamtoYzQxSy9yTFI0MXA0YlZEeUkwczAxRjJ4SGx5VkFaanJOb0R0NzBFTHZlR01ydzNwa0dRa1hYMHhXa2cxamtsMjJ4U285aW1NSTZPdCtoZEt1QlRIQWNMbGtWREZnTUxaQktPS253dElWQT09LS1LRTJSV2lIS2h2SlRmZ0ErWVV3MFN3PT0%3D--48a72401544ab10ca5d28e041afcef67ff0d8838',
        'Host': 'github.com',
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

    def gen_urls(self, start=1, stop=20):
        urls = ['https://github.com/search?l=Python&o=desc&p={p}&q=spider&s=&type=Repositories'.format(p=p) for p in
                range(start, stop)]
        return urls

    def parse_resultcnt(self, response):

        a = response.xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li')

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
