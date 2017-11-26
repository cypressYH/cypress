# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:12:35 2017

@author: 彥賢lab
"""

import xml.etree.ElementTree as ET
import csv
import os

dirdig = 20171123
pathod = "D:\\VDHistory"
pathnw = "C:\\Users\\mis\\Desktop\\hackerthon\\data"
    
def transmit(dirdig) :
    namenum = 0
    ct = 0
    while  namenum < 2360:        #以秒為單位
        dirname = "vd_value5_" + "%04d" % namenum       #檔名
        print(dirname)
        try :
            tree = ET.parse(pathod + '\\' + str(dirdig) + '\\' + dirname + '.xml')      #讀XML
        except Exception:      #出現意外就跳下一檔案
            ct += 1
            namenum += 5
            if ct == 60 :   #60秒
                ct = 0
                namenum += 40
            continue
        root = tree.getroot()   #找tree的root位置
        if not os.path.isdir(pathnw + '\\' + str(dirdig)):      #自動新增資料夾
            os.mkdir(pathnw + '\\' + str(dirdig))
        Infos_data = open(pathnw + '\\' + str(dirdig) + '\\' + dirname + '.csv', 'w', newline='')    #存成CSV   
        csvwriter = csv.writer(Infos_data)
        Infos_head = []     #attr 名稱
        count = 0
        count1 = 0
        for member in root[0].findall('Info') :       #從info節點下去找
            for member1 in member.findall('lane') :     #從 lane節點下去找
                info = []             #data 內容 , list 格式
                boolin1 = "false"          #vdid 找到後為true
                boolin2 = "true"          #datacollecttime 找到後為true
                boolin3 = "false"          #轉換成 level 後為true
                if count == 0 :
                    if count1 == 0 :
                        for key, value in member.attrib.items() : 
                            if key == "vdid" :
                                vdid = key                                                               
                        Infos_head.append(vdid)            #vdid
                        nlevel = "level"        
                        Infos_head.append(nlevel)          #level
                        nvsdir = "vsrdir"
                        Infos_head.append(nvsdir) #vsdir
                        csvwriter.writerow(Infos_head)     #寫入CSV中
                        count += 1
                        count1 += 1
                for key, value in member.attrib.items() :
                    if key == "vdid" :
                        if value == "thbVD-15-0030-036-01" : #大溪
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-15-0030-041-02" : #平鎮
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-15-0030-047-01" : #龍潭
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-16-0030-071-01" : #橫山
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-16-0030-077-01" : #竹東
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-16-0030-077-02" : #北埔
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-16-1180-024-01" : #關西
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-21-0030-094-01" : #峨嵋、頭份
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-21-0130-016-01" : #三灣
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-21-0030-105-01" : #獅潭、南庄
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-21-0030-130-01" : #大湖
                            vdid = value                           
                            boolin1 = "true"
                        if value == "thbVD-21-0130-048-01" : #三義
                            vdid = value
                            boolin1 = "true"
                        if value == "thbVD-22-0030-151-01" : #卓蘭
                            vdid = value
                            boolin1 = "true"
                info.append(vdid)      #vdid
                for key, value in member1.attrib.items() :     #轉換level             
                    if key == "speed" :
                        speed = value
                        if int(speed) > 50 :
                            level = 1
                            boolin3 = "true"
                        if int(speed) < 51 and int(speed) > 30 :
                            level = 2
                            boolin3 = "true"
                        if int(speed) < 31 :
                            if int(speed) < 0:
                                level = 0
                            else :
                                level = 3
                            boolin3 = "true" 
                    if key == "vsrdir" :
                        vsrdir = value
                info.append(level)
                info.append(vsrdir)
                #print(boolin1, boolin2, boolin3)
                if boolin1 == "true" and boolin2 == "true" and boolin3 == "true" :    #三個boolin皆為true才存入CSV
                    #print(info)
                    csvwriter.writerow(info) 
        ct += 1
        namenum += 5
        if ct == 60 :                #60秒
            ct = 0
            namenum += 40
        Infos_data.close()
               
while dirdig < 20171126:  #日期
    print(str(dirdig))
    transmit(dirdig)
    dirdig += 1
    if dirdig == 20161032 :
        dirdig = 20161101
    if dirdig == 20161131 :
        dirdig = 20161201
    if dirdig == 20161232 :
        dirdig = 20170101
    if dirdig == 20170132 :
        dirdig = 20170201
    if dirdig == 20170229 :
        dirdig = 20170301
    if dirdig == 20170332 :
        dirdig = 20170401
    if dirdig == 20170431 :
        dirdig = 20170501
    if dirdig == 20170532 :
        dirdig = 20170601
    if dirdig == 20170631 :
        dirdig = 20170701
    if dirdig == 20170732 :
        dirdig = 20170801
    if dirdig == 20170832 :
        dirdig = 20170901
    if dirdig == 20170931 :
        dirdig = 20171001
    if dirdig == 20171032 :
        dirdig = 20171101