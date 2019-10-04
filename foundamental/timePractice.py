import time

# localtime：秒转时间元组  mktime：时间元组转秒

print('time:', dir(time), '\n')

a = time.time()

b = time.localtime()       # struct_time 省略参数表示当前时间的localtime， 加参数表示指定时间的
f = time.mktime(b)

c = time.strftime('%Y/%m/%d', b)    # str
g = time.strptime(c, '%Y/%m/%d')    # struct_time
print(c)

e = time.ctime(a)
h = time.asctime(b)

print(time.timezone, time.daylight)

d = 3