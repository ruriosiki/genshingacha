# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:25:40 2021

@author: ruriosiki
"""

import random
import os
import configparser
 
class CharacterUP():
    
    def __init__(self):
        
        
        self.up_five = ["温迪"]
        self.other_five = ["刻晴","莫娜","七七","迪卢克","琴"]
        self.up_four = ["砂糖","雷泽","诺艾尔"]
        self.ren_four = ["砂糖", "诺艾尔", "菲谢尔", "行秋", "香菱",
                         "雷泽", "芭芭拉", "重云", "班尼特", "凝光",
                         "辛焱","迪奥娜","北斗"]
        self.wuqi_four = ["弓藏", "绝弦", "昭心", "流浪乐章", "西风长枪",
                          "雨裁", "钟剑", "匣里龙吟", "笛剑", "祭礼弓",
                          "西风猎弓", "祭礼残章", "西风秘典", "匣里灭辰", "祭礼大剑",
                          "西风大剑", "祭礼剑", "西风剑"]
        
        self.other_four = self.ren_four.copy()
        
        for ren in self.up_four:
            if ren in self.ren_four:
                self.other_four.remove(ren)
            
            
        self.fournum = '1'
        self.fivenum = '1'
        self.fiveup =  '0'
        self.fourup =  '0' 
        self.fourren = '1'
        self.fourwuqi = '1'
        
        self.fournum_0 = '1'
        self.fivenum_0 = '1'
        self.fiveup_0 =  False
        self.fourup_0 =  False 
        self.fourren_0 = '1'
        self.fourwuqi_0 = '1'
        
        self.threeweight = 9430
        self.fourweight = 510
        self.fiveweight = 60
        
        self.shilianlist = []
        
        self.threeallnum = 0
        self.fourallnum = 0
        self.fiveallnum = 0
        self.fourupnum = 0
        self.fiveupnum = 0
        self.gachanum = 0
        
        realpath=os.path.dirname(os.path.realpath(__file__))    
        self.base_dir = os.path.abspath(realpath)
        
        try:
            self.read_info()
        except:
            self.init_info()
    
    def count(self):
        conf_path = self.base_dir + '\\config.ini'
        conf = configparser.ConfigParser()
        conf.read(conf_path)
        
        threeallnum = conf.get("CharacterUP_statistics" ,"threeallnum")
        fourallnum = conf.get("CharacterUP_statistics" ,"fourallnum")
        fiveallnum = conf.get("CharacterUP_statistics" ,"fiveallnum")
        fourupnum = conf.get("CharacterUP_statistics" ,"fourupnum")
        fiveupnum = conf.get("CharacterUP_statistics" ,"fiveupnum")
        gachanum = conf.get("CharacterUP_statistics" ,"gachanum")
        
        countlist = [int(threeallnum),int(fourallnum),int(fiveallnum),int(fourupnum),int(fiveupnum),int(gachanum)]
        return countlist
    
    def kachi(self,threeweight,fourweight,fiveweight):
    
        list_raw = ['3']*threeweight + ['4']*fourweight +['5']*fiveweight
        random.shuffle(list_raw)
        random.shuffle(list_raw)
        random.shuffle(list_raw)
        
        num = int(random.random()*10000)
        result = list_raw[num]
        
        return result
    
    #每一次抽取
    def every(self,fournum,fivenum):     
        
        if fournum >= 9 and fournum <= 10:
            self.fourweight = 510+5100*(fournum-8)
        elif fournum < 9 and fournum >= 1:
            self.fourweight = 510
        else:
            print('fournum数据错误')
            
        
        if fivenum >= 74 and fivenum <= 90:
            self.fiveweight = 60+600*(fivenum-73)
    
        elif fivenum < 74 and fivenum >= 1:
            self.fiveweight = 60
    
        else:
            print('fivenum数据错误')
            
            
        if self.fiveweight<= 10000:
            
            
            if self.fiveweight + self.fourweight >=10000:
                self.threeweight = 0
                self.fourweight = 10000 - self.fiveweight
            else:
                self.threeweight = 10000-self.fiveweight-self.fourweight
                
        else:
            self.fiveweight = 10000
            self.threeweight = 0
            self.fourweight = 0
            
        result = self.kachi(self.threeweight,self.fourweight,self.fiveweight)
        
        return result
    
    #重置配置文件
    def init_info(self):
        
        conf_path = self.base_dir + '\\config.ini'
        conf = configparser.ConfigParser()
        conf.read(conf_path)
        if "CharacterUP_basedata" not in conf.sections():
            conf.add_section("CharacterUP_basedata")
            
        conf.set("CharacterUP_basedata", "fournum", "1")
        conf.set("CharacterUP_basedata", "fivenum", "1")
        conf.set("CharacterUP_basedata", "fiveup", "0")
        conf.set("CharacterUP_basedata", "fourup", "0")
        conf.set("CharacterUP_basedata", "fourren", "1")
        conf.set("CharacterUP_basedata", "fourwuqi", "1")
        
        if "CharacterUP_statistics" not in conf.sections():
            conf.add_section("CharacterUP_statistics")
        
        conf.set("CharacterUP_statistics" ,"threeallnum" ,"0")
        conf.set("CharacterUP_statistics" ,"fourallnum" ,"0")
        conf.set("CharacterUP_statistics" ,"fiveallnum" ,"0")
        conf.set("CharacterUP_statistics" ,"fourupnum" ,"0")
        conf.set("CharacterUP_statistics" ,"fiveupnum" ,"0")
        conf.set("CharacterUP_statistics" ,"gachanum" ,"0")
    
        conf.write(open(conf_path, 'w'))
        
        self.read_info()
        #txt_path = base_dir + '\\result.txt'
        
    def save_info(self):
        
        conf_path = self.base_dir + '\\config.ini'
        conf = configparser.ConfigParser()
        conf.read(conf_path)
        conf.set("CharacterUP_basedata", "fournum", self.fournum)
        conf.set("CharacterUP_basedata", "fivenum", self.fivenum)
        conf.set("CharacterUP_basedata", "fiveup", self.fiveup)
        conf.set("CharacterUP_basedata", "fourup", self.fourup)
        conf.set("CharacterUP_basedata", "fourren", self.fourren)
        conf.set("CharacterUP_basedata", "fourwuqi", self.fourwuqi)
        
        conf.set("CharacterUP_statistics" ,"threeallnum" ,str(self.threeallnum))
        conf.set("CharacterUP_statistics" ,"fourallnum" ,str(self.fourallnum))
        conf.set("CharacterUP_statistics" ,"fiveallnum" ,str(self.fiveallnum))
        conf.set("CharacterUP_statistics" ,"fourupnum" ,str(self.fourupnum))
        conf.set("CharacterUP_statistics" ,"fiveupnum" ,str(self.fiveupnum))
        conf.set("CharacterUP_statistics" ,"gachanum" ,str(self.gachanum))
        
        conf.write(open(conf_path, 'w'))
    
    def read_info(self):
        
        conf_path = self.base_dir + '\\config.ini'
        conf = configparser.ConfigParser()
        conf.read(conf_path)
        
        self.fournum = conf.get("CharacterUP_basedata", "fournum")
        self.fivenum = conf.get("CharacterUP_basedata", "fivenum")
        self.fiveup = conf.get("CharacterUP_basedata", "fiveup")
        self.fourup = conf.get("CharacterUP_basedata", "fourup")
        self.fourren = conf.get("CharacterUP_basedata", "fourren")
        self.fourwuqi = conf.get("CharacterUP_basedata", "fourwuqi")
        
        self.threeallnum = int(conf.get("CharacterUP_statistics" ,"threeallnum"))
        self.fourallnum = int(conf.get("CharacterUP_statistics" ,"fourallnum"))
        self.fiveallnum = int(conf.get("CharacterUP_statistics" ,"fiveallnum"))
        self.fourupnum = int(conf.get("CharacterUP_statistics" ,"fourupnum"))
        self.fiveupnum = int(conf.get("CharacterUP_statistics" ,"fiveupnum"))
        self.gachanum = int(conf.get("CharacterUP_statistics" ,"gachanum"))
        
        
    def getfive(self):
        #计算保底
        if self.fiveup_0 == False:
            
            five_raw = ['up']*5 + ['ren']*5
            random.shuffle(five_raw)
            num = int(random.random()*len(five_raw))
            result = five_raw[num]
            
            if result == 'up':
                
                self.fiveupnum += 1
                
                if len(self.up_five) == 1:
                    self.fiveup = '0'
                    five_result = self.up_five[0]
                
                else:
                    
                    random.shuffle(self.up_five)
                    five_result = self.up_five[int(random.random()*len(self.up_five))]
                    self.fiveup = '0'
                
            if result == 'ren':
                
                random.shuffle(self.other_five)
                random.shuffle(self.other_five)
                five_result = self.other_five[int(random.random()*len(self.other_five))]
                self.fiveup = '1'
           
                
        elif self.fiveup_0 == True:
            
            self.fiveupnum += 1
            
            if len(self.up_five) == 1:
                    self.fiveup = '0'
                    five_result = self.up_five[0]
                    
                
            else:
                
                random.shuffle(self.up_five)
                random.shuffle(self.up_five)
                five_result = self.up_five[int(random.random()*len(self.up_five))]
                self.fiveup = '0'
            
        else:
            pass            
            
        if self.fiveup == '0':
            self.fiveup_0 = False
        if self.fiveup == '1':
            self.fiveup_0 = True
        
        return five_result             

    def getfour(self):
        
        #平滑机制
        if self.fourren_0 >= 18:
            fourrenweight = 255 +2550*(self.fourren_0-17)
            fourwuqiweight = 255
            
        elif self.fourwuqi_0 >= 18:
            
            fourwuqiweight = 255 +2550*(self.fourwuqi_0-17)
            fourrenweight = 255
        else:
            fourrenweight = 255
            fourwuqiweight =255
            
        #计算保底和抽出具体的东西
        if self.fourup_0 == False:
            
           four_raw = ['up']*fourrenweight*5 + ['ren']*fourrenweight*5 + ['wuqi']*fourwuqiweight*10
           
           random.shuffle(four_raw)
           random.shuffle(four_raw)
           num = int(random.random()*len(four_raw))
           result = four_raw[num]
           
           if result == 'up':
               random.shuffle(self.up_four)
               random.shuffle(self.up_four)
               four_result = self.up_four[int(random.random()*len(self.up_four))]
               self.fourup = '0'
               self.fourupnum += 1
               
           
           if result == 'ren':
               random.shuffle(self.other_four)
               random.shuffle(self.other_four)
               four_result = self.other_four[int(random.random()*len(self.other_four))]
               self.fourup = '1'
               
           
           if result == 'wuqi':
               random.shuffle(self.wuqi_four)
               random.shuffle(self.wuqi_four)
               four_result = self.wuqi_four[int(random.random()*len(self.wuqi_four))]
               self.fourup = '1'
               
           
        if self.fourup_0 == True:
            
            random.shuffle(self.up_four)
            random.shuffle(self.up_four)
            four_result = self.up_four[int(random.random()*len(self.up_four))]
            self.fourup = '0'
            self.fourupnum += 1
        
        if self.fourup == '0':

            self.fourup_0 = False
        
        if self.fourup == '1':
            
            self.fourup_0 = True
        
        return four_result
            
    def shilian(self):
        
        self.fournum_0 = int(self.fournum)
        self.fivenum_0 = int(self.fivenum)
        self.fourren_0 = int(self.fourren)
        self.fourwuqi_0 = int(self.fourwuqi)
        self.fiveup_0 = bool(int(self.fiveup))
        self.fourup_0 = bool(int(self.fourup))
        
        self.shilianlist = []
        
        for i in range(10):
            
            resultnum = self.every(self.fournum_0,self.fivenum_0)
            
            if resultnum == '3':
                
                self.threeallnum += 1
                self.fournum_0 += 1
                self.fivenum_0 += 1
                
                self.shilianlist.append('三星')
                
            if resultnum == '4':
                self.fourallnum += 1
                four_result = self.getfour()
                
                self.fivenum_0 += 1 
                self.fournum_0 = 1
                
                self.shilianlist.append(four_result)
                
               
            if resultnum == '5':
                self.fiveallnum += 1
                five_result = self.getfive()
                
                self.fournum_0 += 1 
                self.fivenum_0 = 1
                
                if self.fournum_0 > 10:
                    self.fournum_0 = 10
                
                self.shilianlist.append(five_result)
                
                
        self.fivenum = str(self.fivenum_0)
        self.fournum = str(self.fournum_0)
        self.gachanum += 10
        
        self.save_info()
        
        return(self.shilianlist)
            
    def danchou(self):
        
        self.fournum_0 = int(self.fournum)
        self.fivenum_0 = int(self.fivenum)
        self.fourren_0 = int(self.fourren)
        self.fourwuqi_0 = int(self.fourwuqi)
        self.fiveup_0 = bool(int(self.fiveup))
        self.fourup_0 = bool(int(self.fourup))
        
        resultnum = self.every(self.fournum_0,self.fivenum_0)
        
        self.gachanum += 1
        
        if resultnum == '3':
            self.threeallnum += 1
            self.fournum_0 += 1
            self.fivenum_0 += 1
            
            self.fivenum = str(self.fivenum_0)
            self.fournum = str(self.fournum_0)
            
            self.save_info()
            
            return('三星')
            
        if resultnum == '4':
            self.fourallnum += 1
            four_result = self.getfour()
            
            self.fivenum_0 += 1 
            self.fournum_0 = 1
            self.fivenum = str(self.fivenum_0)
            self.fournum = str(self.fournum_0)
            
            self.save_info()
            return(four_result)
               
        if resultnum == '5':
            self.fiveallnum += 1
            five_result = self.getfive()
            
            self.fournum_0 += 1 
            self.fivenum_0 = 1
            
            if self.fournum_0 > 10:
                self.fournum_0 = 10
            
            self.fivenum = str(self.fivenum_0)
            self.fournum = str(self.fournum_0)
            
            
            self.save_info()
            
            return(five_result)