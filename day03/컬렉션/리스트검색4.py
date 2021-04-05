
food_list = ['맛나피자','새로피자','대왕햄버거','군대햄버거']
# print(food_list[-4:-2])
# last_food = food_list[-1]
# print(last_food[-3:])
# print(food_list[2:])
last_food = food_list[-1]
print(last_food[2:])
print(food_list.count('피자'))
#피자집 개수, 햄버개 개수 프린트
print('맛나' in '맛나피자')
data = ' abc'
data2 = data.strip()

print('---------------')
#누적시키는 변수는 반복문안에 넣으면 안된다.

for x in food_list:
    if '피자' in x:
        pizza = pizza + 1
    elif'햄버거' in x:
        ham = ham + 1
print('피자 가게 개수: ', pizza)
print('햄버거 가게 개수: ', ham)

print('=========================')

pizza = 0
ham = 0

for x in food_list:
    food = x[2:] #피자, 햄버거
    if food == '피자':
        pizza = pizza + 1
    elif food == '햄버거':
        ham = ham + 1
print('피자 가게 개수: ', pizza)
print('햄버거 가게 개수: ', ham)


print('---------------')
for i in range(len(food_list)):
    print('피자' in food_list[i])