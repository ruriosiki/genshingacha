# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:55:28 2021

@author: ruriosiki
"""
import genshingacha

cup = genshingacha.CharacterUP()

#单抽函数，返回字符
#cup.danchou()


#十连函数,返回列表
#a = cup.shilian()
#print(a)


#重置抽卡记录
cup.init_info()


'''-----------------------------------------'''
#计算需要多少次十连抽到五星角色
def wuxin(fivelist):
    for i in range(20):
        fin_result = cup.shilian()
        if list(set(fin_result).intersection(set(fivelist))) != []:
            print(i+1)
            print(fin_result)
            break
        

fivelist = ["温迪","刻晴","莫娜","七七","迪卢克","琴"]
#wuxin(fivelist)


'''-----------------------------------------'''
#计算需要多少次十连抽到对应角色

def wuxinup(character):
    
    for i in range(100):
        
        fin_result = cup.shilian()
        if character in fin_result:
            print(i+1)
            break
    
    print(fin_result)
    
#wuxinup("刻晴")



'''-----------------------------------------'''
#统计概率

#十连抽卡次数
num = 10

def count_pro():
    for i in range(num):
        cup.shilian()
    
    #返回整型 countlist = [所有三星的数量,所有四星的数量,所有五星的数量,所有四星up的数量,所有五星up的数量,抽卡数]
    count_list = cup.count()
    
    fivepro = count_list[2]/count_list[5]
    fourpro = count_list[1]/count_list[5]
    fouruppro = count_list[3]/count_list[5]
    fiveuppro = count_list[4]/count_list[5]
    
    #获得五星up概率，五星概率，四星up概率，四星概率
    print(fiveuppro,fivepro,fouruppro,fourpro)

   
#count_pro()