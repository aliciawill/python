# import bs4
from bs4 import BeautifulSoup
from urllib import request
import datetime


year = input('순위 조회를 원하는 날짜를 입력해주세요(예: 20210128) : ')
print('---------------------------------')
# year_list = []
# if len(year_list) > 8:
# elif year[:4] > 2021:
# elif year[4:6] > 13:
# elif year[5:] > 31:

name_list = ['조회순', '평점순(현재상영영화)', '평점순(모든영화)']
code_list = ['cnt', 'cur', 'pnt']
for index in range(len(code_list)):
    con = request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel='+code_list[index]+'&date='+ year) #연결부품 획득

    name = name_list[index]
    doc = BeautifulSoup(con, 'html.parser')

    td_title = doc.select('td.title')
    td_point = doc.select('td.point')

    print('순위배정기준:',name)

    if code_list[index] == 'cnt':
        for rank in range(len(td_title)):
            tit = td_title[rank].text
            print('순위' , rank+1 , ":" , tit.strip())
            file = open(name_list[index] + '.txt', 'w')
            file.write('제목: ' + tit.strip() + '\n')
            file.close()
    elif code_list[index] == 'cur' or 'pnt':
        for rank in range(len(td_point)):
            tit = td_title[rank].text
            tp = td_point[rank].text
            print('순위' , rank+1 , '평점) ' , tp , ":" , tit.strip())
            file = open(name_list[index] + '.txt', 'w')
            file.write('제목:' + tit.strip() + tp.strip() + '\n')
            file.close()
    else :
        break

    print('---------------------------------')