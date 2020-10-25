# @Time = 2020/10/25 23:06
# @Author = Eva
# @File = XuZhu.py

from commit_lg4.TongLao import TongLao
#定义XuZhu类继承TongLao类
class XuZhu(TongLao):
    def __init__(self,tonglao_hp,tonglao_power,enemy_hp,enemy_power):
        super().__init__(tonglao_hp,tonglao_power,enemy_hp,enemy_power)

    def read(self):
        print("罪过罪过！")

tonglao =TongLao(10,10,200,200)
tonglao.see_people("李秋水")
tonglao.fight_zms()
xuzhu = XuZhu(10,10,20,20)
xuzhu.read()

