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

def update(id, tel):
    #1. mysql과 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    #2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    #3. sql문을 만들어서 전송함.
    sql = "update member set tel = %s where id = %s"
    cur.execute(sql, (tel, id)) #tuple로 넣어주어야 한다.

    #4. auto-commit이 안된다. 수동으로 반영시켜야 한다.
    con.commit()
    con.close()

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






