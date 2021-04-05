
print('hello')

print('안녕하세요.', end=' ')
print('저는 홍길동입니다.')

# 설명을 씀, 컨트롤 + /, comment, 주석
# 입력: 데이터를 가지고 와야감.
# 처리: 적절한 처리
# 출력: 처리한 결과를 내보는 일(모니터, 파일, db저장, 네트워크 전송)

name = input('이름을 입력하세요 >> ') #간단한 처리(기호를 씀): 연산=> 연산자
# = : 대입연산자

print(name)

age = input('나이를 입력 >> ')
print(age)

company = input('소속을 입력 >> ')
print(company)

location = '신촌'

number = 2

height = 195.5

food_lunch = True

age2 = input('나이 입력>> ') #100 
#컴퓨터에서 입력한 데이터는 타입을 무조건 스트링으로 인식!
#스트링을 정수로 바꾸어쓰는(강제 캐스팅) 결정은 프로그래머가 한다.
print('내년 나이는 ', int(age2) + 1)

# 두수를 입력을 받아서, 사칙연산을 해보세요.
n1 = int(input('숫자1>> '))
n2 = int(input('숫자2>> '))

print('두 수의 합은 ', n1 + n2) #산술연산자(더하기 연산)
print('두 수의 차는 ', n1 - n2)
print('두 수의 곱은 ', n1 * n2) #아스테리크, 에스테리크
print('두 수의 나누셈은 ', n1 / n2)
print('두 수의 나누셈은 ', n1 // n2)

me = '커피'
me2 = '우유'
print(me + me2) #문자열로 결합시켜라(결합연산자)

price = 1000

print(me + '가격은 ' + str(price) + '원')

coffee_price = int(input('커피값 입력: '))
coffee_count = int(input('커피 인원수 입력: '))
sum = coffee_price * coffee_count #변수(저장공간, 저장공간이름=>변수명)

if sum >= 20000: #True
  print('20000원 이상입니다.')
  print(sum - 2000, '원 결제하세요.')
else: #False
  print('20000원 미만입니다.')
  print(sum, '원 결제하세요.')

a = '홍길동'
b = '홍길동'
print(a == b)

if a == b:#True일때만!
  print('동일한 사람')
else:#False인 모든 상황!
  print('다른 사람')

money = int(input('1년 만기 정기 예금을 얼마나 예치하시겠습니까? '))

money2 = input('1년 만기 정기 예금을 얼마나 예치하시겠습니까? ')
money3 = int(money2)

print('원금이 ', money, '원이신구요.!' )

print('이자는 ',int(money * 0.1),'원이신구요.!' )

print('원리합계는 ', money + int(money * 0.1), '원이신구요.!' )

sticker_price = 1000
sticker_count = 3

book_price = 2500
book_count = 4

sum = sticker_price * sticker_count + book_price * book_count

print('총 결제 금액은 ', sum)

discount = sum * 0.1 #할인받는 금액

print('할일받는 금액 ', discount)

print('내가 낸 금액은 ', int(sum - discount))

id = 'root'

id2 = input('로그인할 id를 입력>> ') #root

if id == id2: #True
  print('로그인되었습니다.')
else:
  print('로그인되지 않았습니다.')

