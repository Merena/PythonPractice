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
Cookie: _octo=GH1.1.1290119782.1559474823; _ga=GA1.2.71546662.1559474842; _device_id=b696399a06253b1b8195ecd257dad20c; tz=Asia%2FShanghai; user_session=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; __Host-user_session_same_site=qSpTxq-6vH8_sF7CWS8Bt81oPxOT5jfkB1T6s8JahbzfZsLc; logged_in=yes; dotcom_user=Merena; has_recent_activity=1; _gat=1; _gh_sess=VGc1ekVkODBJNHp1b2xoc1JaWXlHNmhLL2dDa1JvNXYrc2RLdDNSZ0wxYUlGQU9jeklLOUFxLzdad2phUGhPbkhWSU5SaUphdnBwYVJjWnNET0ZUcHJXSTB5N29BcEY4aHpPNmhqNjd6Z0xIeXIzZVNpd3pzTEw1VmdpTVl1ejRsNll2THhlNjF6dUZMbnF3dmJQL2FtNFhFY09rY0tiajIrZHErbHU1eGd0QnN3eE9TTmtHUWVhdG8zdXNZYnhjWmwwWGxBRUptai9aQlJ6OHhmMjM3dFFPK0F1YksrRExzdkFYc2NFckZ5UnhudnpiQmJMcGlVeEZWV3ltaEdiQ01RT3BvOXc1a0VOYkhHdHRRcEd3SENBSlBXVVR4UEdnZ2h1OEMzcFoxaWx4dWNuRGx1a0VFcXBqcERQQVdPNzUtLTc3bnV5NjRmdm1McGdUWmpzbFVnSUE9PQ%3D%3D--836221a078de8cb9f19fe4d5ac3f25d35d01f439
Host: github.com
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
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
