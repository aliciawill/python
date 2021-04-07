class Person:
    name = None
    age = 0

    def eat(self):
        print('먹다')

    def __str__(self):
        return self.name + ' ' + self.age

class Man(Person):
    speed = 0

    def run(self):
        print('빨리 달리다')

    def __str__(self):
        return self.name + ' ' + self.age + ' ' + self.speed

class SuperMan(Man):
    fly = False

    def sky(self):
        print('하늘을 날다.')

    def __str__(self):
        return self.name + ' ' + \
               self.age + ' ' + \
               self.speed + ' ' + \
               self.fly



