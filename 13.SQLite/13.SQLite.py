# -*- coding: utf-8 -*-
import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value='0'
    return float(value)
conn=sqlite3.connect('food.db')#创建数据库链接
curs=conn.cursor()#创建游标
#创建表
curs.execute('''
create table IF NOT EXISTS food(
id        TEXT   PRIMARY KEY ,
desc     TEXT ,
water     FLOAT,
kcal      FLOAT,
protein   FLOAT,
fat       FLOAT,
ash       FLOAT,
carbs     FLOAT,
fiber     FLOAT,
sugar     FLOAT
)
''')
truntablequery='DELETE FROM food'
curs.execute(truntablequery)
query ='insert into food VALUES (?,?,?,?,?,?,?,?,?,?)'
for line in open('ABBREV.txt'):
    fields=line.split('^')
    vals=[convert(f) for f in fields[:10]]
    curs.execute(query,vals)
conn.commit()

selectquery='SELECT *  FROM food WHERE  %s'%'kcal<=100 and fiber>=10 and sugar order by sugar'
curs.execute(selectquery)
names=[n[0] for n in curs.description]#curs.description 对表结构的描述，列名
for row in curs.fetchall():#curs.fetchall()获取所有结果，返回的是一个二维列表[[1,2,3],[4,5,6],[7,8,9]]
    for pair in zip(names,row):
        print '%s:%s'%pair
    print ''
conn.close()



