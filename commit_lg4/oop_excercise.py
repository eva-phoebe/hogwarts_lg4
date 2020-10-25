# # @Time = 2020/10/25 11:49
# # @Author = Eva
# # @File = oop_excercise.py
#

"""1/定义类Cat"""

class Cat():
    #构造函数中定义name和age参数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #定义catch方法
    def catch(self):
        print(self.name.title() + "is catch the mouse.")
    #定义sleep方法
    def sleep(self):
        print(self.name.title() + "is sleeping now.")

#实例化，传递参数
my_pet = Cat("小福", 5)
#调用catch方法和sleep方法
my_pet.catch()
my_pet.sleep()

"""2/定义类People"""


class People():
    #构造函数中定义country和sex参数
    def __init__(self, country, sex):
        self.country = country
        self.sex = sex
    #定义work方法
    def work(self):
        print(f"这是个{self.sex}程序员")
        print(f"这是个来自{self.country}的程序员")

#实例化，传递参数
RD = People("中国", "女")
#调用work方法
RD.work()

"""3/定义类Ball"""


class Ball():
    def __init__(self, name):
        self.name = name

    #定义滚动（roll_over）方法
    def roll_over(self):
        print(f"{self.name}可以滚动")

    #定义弹跳（jump方法）
    def jump(self):
        print(f"{self.name}可以弹跳")


my_ball = Ball("Basketball")
my_ball.roll_over()
my_ball.jump()

"""4/定义类School"""
class School():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    #定义教育情况（education）方法
    def education(self):
        print(self.name.title()+" is the school of "+self.type.title())
my_school = School("Hogwarts","magic")
my_school.education()



"""5/定义类Car"""
class Car():
    def __init__(self, power, color):
        self.power = power
        self.color = color

    #定义行驶（run）方法
    def run(self):
        print(f"{self.power}的车会跑")

    #定义安全（save）方法
    def save(self):
        print(f"{self.color}颜色的车是比较安全的")

#实例化，传递车辆动力和颜色参数
my_car = Car("油电混合","蓝色")
my_car.run()
my_car.save()


