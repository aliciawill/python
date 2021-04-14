names = ['홍길동', '김길동', '박길동']
ages = [100, 200, 300]

total_list = list(zip(names, ages))
print(len(total_list))
print(tuple(total_list))

names2 = [[111, 111], [222, 222], [444, 333]]
ages2 = [[100, 1], [200, 2], [300, 3]]

def add(data1, data2):
    return data1 + data2

total_list2 = list(map(add, names2, ages2))
print(len(total_list2))
print(total_list2)

print('---------------------------------')
def add2(data1, data2):
    return (data1, data2)

total_list3 = list(map(add2, names, ages))
print(len(total_list3))
print(total_list3)