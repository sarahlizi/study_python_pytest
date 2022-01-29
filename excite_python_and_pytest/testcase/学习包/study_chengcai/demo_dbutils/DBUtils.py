import pymysql

class DBUtils:
    count=-1

    #封装链接对象和游标对象
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('工具类链接出现一场，请检查DBUtils中的__init__方法')
            print(e)

    #封装关闭游标和关闭链接对象
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 封装 结果集有多少条数据
    # 如果execute中只传一个参数,我们需要运行 cursor.execute(sql)
    # 如果execute中传2个参数,我们需要运行 cursor.execute(sql,占位符数据)
    def find_count(self,sql,params=None):
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
                return self.count
            elif params is not None:
                return self.cursor.execute(sql, params)
        except Exception as e:
            print('查询条目数失败！',e)

    # 封装   增删改
    # 如果execute中只传入一个参数,我们需要运行cursor.execute(sql)
    # 如果execute中传入2个参数,我们需要运行cursor.execute(sql,params)
    def cud(self,sql,params=None):
        try:
            if params is None:
                self.count=self.cursor.execute(sql)
            if isinstance(params,tuple):
                self.count=self.cursor.execute(sql,params)
            if isinstance(params,list):
                self.count=self.cursor.executemany(sql,params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print('增删改查执行失败！',e)

    #封装  查询一条数据
    def find_one(self,sql,params=None):
        try:
            if params is None:
                self.cursor.execute(sql)
                return self.cursor.fetchone()
            elif params is not None:
                self.cursor.execute(sql,params)
                return self.cursor.fetchone()
        except Exception as e:
            print('查询所有数据执行失败',e)

if __name__=='__main__':
    db =DBUtils()
    print(db)

    count = db.cud('deletee from account')
    print(count)

    count = db.cud('insert into account(name,age,nickName) values(%s,%s,%s)', ('xiaohong', 20, 'honghong'))
    db.conn.commit()
    print(count)

    count = db.cud('insert into account(name,age,nickName) values(%s,%s,%s)',
                   [('xiaobai', 18, 'baibai'), ('xiaohei', 20, 'heihei'), ('xiaoxu', 25, 'xuxu')])
    print(count)

    data = db.find_one('select * from account')
    print(data)

    data = db.find_one('select * from account where name=%s', ('xiaohei',))
    print(data)

    data = db.find_all('select * from account')
    print(data)

    data = db.find_all('select * from account where age=%s', (20,))
    print(data)

    db.close()