'''
Python 3最重要的新特性大概要算是对文本和二进制数据作了更为清晰的区分。文本总是Unicode（16进制），由str类型表示，
二进制数据则由bytes类型表示。Python 3不会以任意隐式的方式混用str和bytes，正是这使得两者的区分特别清晰。
你不能拼接字符串和字节包，也无法在字节包里搜索字符串（反之亦然），也不能将字符串传入参数为字节包的函数（反之亦然）.

bytes is immutable, byteArray is mutable
'''

k1 = '70周年'
print(type(k1))

m1 = k1.encode('utf8')
print(type(m1))

r1 = m1.decode('utf8')
print(type(r1))

s1 = b'kerp'    # 这个是bytes类型



