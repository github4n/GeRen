import pymysql

db = pymysql.connect(host='localhost',user='root',password='1784210334',port=3306,db='spiders')

cursor = db.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))')

db.close()