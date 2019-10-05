#
# https://zhuanlan.zhihu.com/p/51608696
#


import redis

redis_conn = redis.Redis(host='127.0.0.1', port= 6379)

redis_conn.set('name_2', 'Zarten_2')
v = redis_conn.get('name_2')
print(v)


redis_conn.mset(name_1= 'Zarten_1', name_2= 'Zarten_2')