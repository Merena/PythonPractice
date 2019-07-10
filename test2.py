# import requests
import re
import json
import os
import urllib
from pathlib import Path
import parsel

os.truncate()
# url = 'http://exercise.kingname.info/ajax_1_backend'
# url2 = 'http://exercise.kingname.info/ajax_1_postbackend'
#
#
# # c1 = requests.get(url).content.decode()
# # c2 = requests.post(url2, json={'name': "xx", 'age': 24}).content.decode()
#
# c3 = requests.get('http://exercise.kingname.info/exercise_ajax_2.html').content.decode()
# c4 = re.findall("secret = '(.*?)'", c3)[0]
#
# js = json.loads(c4)
# c5 = js['code']
#
# print(c5)
# print(c4)
# print(c1)
# print(c2)
os.path.abspath('~')
os.path.getatime()

a = Path("/Users/mhm/Documents/python  standard  library.pdf")
print(a)

print(a.exists())
print(a.group())
print(a.home())
print(a.is_dir())
print(a.is_fifo())
print(a.is_file())
print(a.is_socket())
a.stem

# with open('text.txt', 'r', encoding='utf-8') as f:
#     content = f.readlines()
#     print(content)