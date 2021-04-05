food = ['아이스크림','아이스아메리카노','생수'] #목록(list)
# hobby = []
print(food[0])
print(food[1])
print(food[2])

for i in range(0, len(food)): #0,1,2
    print(food[i], end=' ')
print()

#
for x in food: #for-each
    print(x, end=' ')
print()

print('목록의 개수는 ', len(food)) #3
########
# 오늘 끝나고 나서,할 일 5가지를 목록으로 만들어보세요.
# 2가지 방식으로 프린트!
todo_list = ['잠자기','코딩','밥','커피','놀기']
for index in range(0, len(todo_list)):
    print(todo_list[index])

for x in todo_list:
    print(x)