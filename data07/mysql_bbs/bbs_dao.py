import pymysql

def create(vo):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into bbs values (%s, %s, %s, %s)'
    result = cur.execute(sql, vo)
    print(result)
    con.commit()
    con.close()

def update(vo):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'update bbs set content = %s where bbsid = %s'
    result = cur.execute(sql, vo)
    print(result)
    con.commit()
    con.close()

def all():
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    sql = "select * from bbs"
    cur.execute(sql)

    # row = cur.fetchone()

    rows = cur.fetchall() # 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    #print(rows)
    print(type(rows))
    # print(rows[0])
    for row in rows:
        print(row)

    con.close()

def read(id):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = "select * from bbs where bbsid = %s"
    cur.execute(sql, id)

    row = cur.fetchone()
    print(row)
    print(type(row))
    print('아이디:', row[0], '제목:', row[1], '내용:', row[2], '글쓴이:', row[3])

    con.close()