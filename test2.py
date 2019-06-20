import requests
import re
import json

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

with open('text.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(content)