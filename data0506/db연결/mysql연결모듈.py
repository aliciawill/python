import pymysql #alt+Enter
#DAO역할 모듈: CRUD(DML)

#정형데이터 => mysql, oracle, sqlite3(관계형 데이터베이스 관리 시스템, RDBMS)
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

def read():
    pass

def update():
    pass

def delete(id):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'delete from member where id = "' + id + '"'
    result = cur.execute(sql)
    print(result)

    con.commit()
    con.close()






