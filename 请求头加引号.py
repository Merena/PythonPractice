"""
使用正则表达式将headers转换为python字典格式的工具函数
"""

import re
headers_str = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Cookie: _octo=GH1.1.1290119782.1559474823; _ga=GA1.2.71546662.1559474842; _device_id=b696399a06253b1b8195ecd257dad20c; tz=Asia%2FShanghai; user_session=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; __Host-user_session_same_site=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; logged_in=yes; dotcom_user=Merena; has_recent_activity=1; _gat=1; _gh_sess=SjJvamlXbjhmdlYxRmorYkNPeGJkdGI1c0VOQWVDa083bUxWdWkvVmcvWnNTVnVlK01tRXZDck56d0FpWno1SDNQZ21mNmZ5RVlHTzQxREVac1BSd0hRRkoxclJjelIvSHFteHFDVFdqVnJwUlhZeE9DVXZWblVoWitqV0I0bmF3WEFMOVVSOFZkZ0o4MXVKT2VTeDFzN0tLMFFncStkTDhFbXpZRmVVL2JsaXhnR0hYM2RJeXkxVFhZTGVxWXp1SzU3NGJScTV1aDhYZUtNNllpMmZyZ1lxWCt1TExkVWo3dFdSNEZYVTVUbz0tLXVFUjNneWlyYVVYaVo0TjZUbmV4Z2c9PQ%3D%3D--a78c7b3ae4f1f7ee1526e0aafa94c585313eda44
Host: github.com
If-None-Match: W/"23a8ee73eea45224f3be70d1a2b0083b"
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36
"""

pattern = '^(.*?): (.*?)$'

for line in headers_str.splitlines():
    print(re.sub(pattern, r"'\1': '\2',",line))


"""
使用chrome console检查css selector/xpath的有效性
https://blog.csdn.net/u010895119/article/details/77186159
$(selector)和$$(selector)
$x(path)
"""
