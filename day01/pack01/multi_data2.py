hobby = []
hobby.append('코딩')
print('개수>> ', len(hobby))
hobby.append('등산')
print('개수>> ', len(hobby))

for _ in range(3): #0, 1, 2
    data = input('당신의 새로운 취미는 >> ')
    hobby.append(data)

print('개수>> ', len(hobby))

for x in hobby:
    print(x)