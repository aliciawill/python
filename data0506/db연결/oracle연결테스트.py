import cx_Oracle

con = cx_Oracle.connect('root/1234@localhost:1521/xe')

cur = con.cursor()
print(cur)

sql = 'insert into MEMBER values ("python2","python","python","python")'
result = cur.execute(sql)
print(result)

con.commit()





