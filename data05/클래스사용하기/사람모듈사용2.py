from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class WomanDay(Person, my.Day):
# 파이썬: 클래스간 다중 상속이 가능하다.
# 자바: 클래스간 단일상속만 가능하다.

    def __init__(self, doing, time, location):
        my.Day.__init__(self, doing, time, location)

    def free(self):
        print('쉬다.!')

if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기', 20, '마포구')
    woman_day1.free()
    woman_day1.eat()
