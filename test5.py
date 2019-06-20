import re
import
content = '多个包括“比特易22222500人投资群”的微信aaaaa群显示，惠轶的轻生与比特币的百'

pp = re.search('易(.*?)人', content, re.S)
print(pp)

a = re.compile('dd')
a.findall()