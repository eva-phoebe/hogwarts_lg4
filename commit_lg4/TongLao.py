# @Time = 2020/10/25 23:02
# @Author = Eva
# @File = TongLao.py


"""定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造"""

#定义天山童姥类TongLao
class TongLao():
    def __init__(self,tonglao_hp,tonglao_power,enemy_hp,enemy_power):
        self.tonglao_hp = tonglao_hp
        self.tonglao_power = tonglao_power
        self.enemy_hp = enemy_hp
        self.enemy_power = enemy_power

    #定义see_people方法
    def see_people(self, name):
        if name == "WYZ":
            print("师弟")
        elif name == "李秋水":
            print("师弟是我的")
        elif name == "丁春秋":
            print("叛徒，我杀了你")

    #定义天山折梅手（fight_zms）方法
    def fight_zms(self):
        #调用折梅手的方法，童姥的武力值（power）就会增加10倍，血量（hp）就会减少一半
        self.tonglao_power = self.tonglao_power * 10
        self.tonglao_hp = self.tonglao_hp/2
        #打斗一个回合
        self.tonglao_hp = self.tonglao_hp - self.enemy_power
        self.enemy_hp = self.enemy_hp - self.tonglao_power
        #打一个回合之后判断谁的血量多
        if self.tonglao_hp >= self.enemy_hp:
            print("天山童姥赢了")
        else:
            print("天山童姥输了")
