import pymysql #alt+Enter

def create(id, pw, name, tel):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member values ("' + id + '","' + pw + '","' + name + '","' + tel + '")'
    result = cur.execute(sql)
    print(result)

    con.commit()
    con.close()

def delete(id):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'delete from member where id = '
    result = cur.execute(sql)
    print(result)

    con.commit()
    con.close()




