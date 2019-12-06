import pymysql
import json


def connectDB():
    db = pymysql.connect("127.0.0.1", "root", "Mm4541520", "test", charset='utf8')
    # conn = mysql.connector.connect(user='root', password='Mm4541520', database='test')
    return db


db = connectDB()


def createTable(db):
    cursor = db.cursor()
    sql = '''
    create table persons
    (id INT PRIMARY KEY NOT NULL,
     name          TEXT NOT NULL,
     age           INT  NOT NULL,
     address       CHAR(50),
     salary        REAL);'''
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    return False


def insertRecords(db):
    cursor = db.cursor()
    try:
        cursor.execute('DELETE FROM persons')
        # 'insert into user (id, name) values (%s, %s)', ('1', 'Michael')
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
                VALUES (1,'PAUL',32,'California',20000.00)")
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
                VALUES (2,'Allen',25,'Texas',15000.00)")
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
                VALUES (3,'Teddy',23,'Norway',30000.00)")
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
    return False


def selectRecords(db):
    cursor = db.cursor()
    sql = 'SELECT name,age,salary FROM persons ORDER BY age DESC'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    fields = ['name', 'age', 'salary']
    records = []
    for row in results:
        records.append(dict(zip(fields, row)))
    return json.dumps(records)


if createTable(db):
    print('成功创建persons表')
else:
    print('表persons已经存在')

if insertRecords(db):
    print('成功插入记录')
else:
    print('插入记录失败')


print(selectRecords(db))
db.close()