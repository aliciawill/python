my_life = '나는 열심히 살자가 인생의 목표예요.!'

print(my_life[0]) #인덱스 0글자 한 개를 추출
print(my_life[0:2]) #인덱스 0~1글자들을 추출

#단어를 분리해내보자.
my_lift_list = my_life.split(sep=' ')
#String의 리스트 ['나는', '열심히',...]
print(my_lift_list[0])
print(my_lift_list[1])

# 1. 주민번호
social_no  = '920101-1037515'
year = social_no[0:2] #String('92')# ->int
year2 = int(year) #92
age = 2021 -  (1900 + year2)
print('당신의 나이는 ', age, '세')

gender = social_no[7] #'1'->문자1글자
if gender == '1'or gender == '3':
    print('남자')
elif gender == '2' or gender == '4':
    print('여자')
else:
    print('잘못된 입력값입니다.')

















