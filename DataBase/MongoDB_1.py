from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建
my_set = db.test_set    #使用test_set集合，没有则自动创建

my_set.insert_one({"name":"zhangsan","age":18})

for i in my_set.find():
    print(i)