try:
    me_file = open("me2.txt", "r", encoding='utf-8')
    lines = me_file.readlines()
    print('읽어온 내용', lines)
    print(type(lines))
    me_file.close()
except IOError:
    print('파일을 읽는 중 에러발생!!!')

print('내가 실행이 되는가......')

