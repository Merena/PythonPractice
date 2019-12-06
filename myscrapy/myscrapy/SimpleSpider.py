from myscrapy.WebRequest import AWebRequest
import requests
import json
from fake_useragent import UserAgent

def validUsefulProxy(proxy):
    """
    检验代理是否可用
    :param proxy:
    :return:
    """
    ua = UserAgent()
    headers = {'User-Agent': ua.random,
     'Accept': '*/*',
     'Connection': 'keep-alive',
     'Accept-Language': 'zh-CN,zh;q=0.8'}

    if isinstance(proxy, bytes):
        proxy = proxy.decode("utf8")
    proxies = {"https": "https://{proxy}".format(proxy=proxy)}
    try:
        r = requests.get('https://guangzhou.anjuke.com/sale/', proxies=proxies, headers=headers, timeout=10, verify=False)
        print(r.text)
        if r.status_code == 200:
            return True
    except Exception as e:
        pass
    return False

def get_random_proxy():
    '''随机从文件中读取proxy'''
    res = requests.get('http://127.0.0.1:5010/get/')
    res.encoding = res.apparent_encoding
    proxy_dic = json.loads(res.text)
    proxy = proxy_dic["proxy"]

    return proxy

# noinspection PyPep8Naming
def testWebRequest():
    i = 0
    while i < 1:
        i += 1
        ip = get_random_proxy()
        # ip = '116.252.39.176:53281'
        print(ip)
        validUsefulProxy(ip)



if __name__ == '__main__':
    testWebRequest()