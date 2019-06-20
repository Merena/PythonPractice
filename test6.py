import requests
import jsonpath
import os

from urllib.request import urlretrieve

content = requests.get("https://www.douyu.com/gapi/rknc/directory/yzRec/2").json()
imgUrl = jsonpath.jsonpath(content, '$..rs1')
names = jsonpath.jsonpath(content, '$..nn')
pageCount = jsonpath.jsonpath(content, '$..pgcnt')
print(imgUrl, names)

path = os.path.abspath('.')+r'/img'
if not os.path.exists(path):
    os.mkdir(path)

for url, name in zip(imgUrl, names):
    urlretrieve(url, path+'/'+name + '.jpg')
print(content)

