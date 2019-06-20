"""
使用正则表达式将headers转换为python字典格式的工具函数
"""

import re
headers_str = """
word: dkd
sizes: 60
fonts: jfcs.ttf
fontcolor: #000000
"""

pattern = '^(.*?): (.*?)$'

for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',',line))
