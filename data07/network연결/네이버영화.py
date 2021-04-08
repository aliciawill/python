import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
#print(result.content)
# result

content = BeautifulSoup(result.content, "html.parser")

# content

dt_list = content.findAll("dt", {"class": "tit"})
# dt_list

print(dt_list[0])
#
# dt_list[0].find("a").text
#
# title = []
# for dt in dt_list:
#     title.append(dt.find("a").text)
#
# # title
#
# len(dt_list)
#
# score_list = content.select('dl.info_star dd div.star_t1 a span.num')
# # score_list
#
# len(score_list)
#
# scores = []
# for score in score_list:
#     scores.append(float(score.text))
#
# # scores
#
#
# df = pd.DataFrame({"영화이름": title, "영화평점": scores})
# # df
#
# print(df)  # dataFrame
# print(df[10:20])  # 10~19
# result = df.describe()  # 자세한 설명
# print(result)
# print(df.head(3))  # 앞에서 3개
# print(df.info())  # 데이터 타입
# print(df.index)  # 인덱스
# print('영화이름')
# print('---------------------')
# print(df['영화이름'])
# print('---------------------')
# print(df['영화평점'])
# print(df.sort_values(by='영화평점', ascending=False))
