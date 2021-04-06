#for문을 사용해보세요.
#range
# 1. range(20) print!
# 2. 1부터 100까지 print!
# 3. 0부터 200까지 print!
# 4. 1부터 100까지 중 2씩 점프해서 print!
# food2 = "감자 고구마 양파 스프 국수 라면"을 다음과 같이 print!
#    감자맛있어! 고구마맛있어! 스프맛있어! 라면 맛있어!
food2 = "감자 고구마 양파 스프 국수 라면"
food_list = food2.split()
for x in food_list:
    if x not in ['양파', '국수']:
        print(x + "맛있어! ", end=' ')
print()
for x in food_list:
    if x == '양파' or x == '국수':
        continue
    print(x + "맛있어! ", end=' ')


