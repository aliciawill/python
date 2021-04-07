import pymysql #alt+Enter

con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
print(con.get_host_info())

cur = con.cursor()
print(cur)

sql = 'insert into member values ("python2","python","python","python")'
result = cur.execute(sql)
print(result)

con.commit()





