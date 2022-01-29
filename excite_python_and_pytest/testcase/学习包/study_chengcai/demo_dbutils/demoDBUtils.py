#1.用来操作mysql数据库
import pymysql

#2.获取链接对象
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='businessdb')
print(conn)

#3.获取游标对象
cursor = conn.cursor()

#4.通过游标对象执行sql语句，把结果集存在cursor里，并返回条目数
'''
知识点：python操作mysql，通过占位符查询
优势：
1.增加SQL代码可读性
2.占位符可以预先编译，提高执行效率
3.防止SQL注入
4.用占位符的目的是绑定变量，这样可以减少数据SQL的硬解析，所以执行效率会提高不少
'''
    #查询语句
count=cursor.execute('select * from account where name= %s and nickName=%s',('xiaohua','huahua'))
print(count)#获取结果集的条目数
conn.commit()
    #插入语句(单条)   execute
count=cursor.execute('insert into account (name,age,nickName) values(%s,%s,%s)',('xiaohua',20,'leilei'))
print(count)#>>> 1
conn.commit()
    #插入语句（多条）   executemany
count=cursor.executemany('insert into accout (name,age,nickName) values(%s,%s,%s)',[('chengxin',20,'chenchen'),('xxgxin',17,'xxchen'),('daxin',20,'dachen')])
print(count)
conn.commit()
    #更新语句
count=cursor.execute('updata account set name=%s where name=%s',('xiaohuang','dahuang'))
print(count)#>>> 1
conn.commit()
    #删除语句
count=cursor.execute('delete from account where name=%s',('dahuang'))
print(count)#>>> 1
conn.commit()

#5.获取查询结果
    #方法一
data=cursor.fetchone()#返回一行数据，并且包装成元组
print(data)
    #方法二
data=cursor.fetchmany(2)#获取结果集的n行数据
print(data)
    #方法三
data=cursor.fetchall()#获取结果集的所有数据
print(data)

#6.关闭游标
cursor.close()

#7.关闭链接
conn.close()




