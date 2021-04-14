num = '123,456'
num = num.replace(',', '')
print(int(num))

def comma(data):
    return int(data.replace(',', ''))

num_list = ['123,456', '333,567']

num_list2 = list(map(comma, num_list))
print(num_list2)

import pandas as pd
names = ['홍길동','김길동','송길동']
hobby = ['1','2','3']
df = pd.DataFrame({'이름': names, '취미':hobby})
print(df)

print(df['이름'].tolist())
print(df['이름'].to_dict())
print(type(df['이름']))









