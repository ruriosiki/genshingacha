根据最新B站ID @一棵平衡树 大佬的理论
参考专栏 https://www.bilibili.com/read/cv10468091

娱乐向原神抽卡模拟器（低仿实际原神卡池）
（现只更新限定角色的UP池模拟）

python3.7和python3.8默认模块皆可运行

#导入角色up池模块
import genshingacha
cup = genshingacha.CharacterUP()

#单抽函数
cup.danchou()
#十连函数
cup.shilian()
#重置抽卡记录
cup.init_info()

#返回整型列表 countlist = [所有三星的数量,所有四星的数量,所有五星的数量,所有四星up的数量,所有五星up的数量,抽卡数]
count_list = cup.count()

更多用法参考
用法.py