from demo_dbutils.DBUtils import DBUtils

db=DBUtils()

count =db.cud('insert into account(name,age) values(%s,%s)',('dahuang',20))

print(count)

db.close()