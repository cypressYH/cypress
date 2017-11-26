# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:28:07 2017

@author: 彥賢lab
"""

import requests
import xml.etree.ElementTree as ET
import csv
import os
import time

rtime = time.strftime("%H%M")
if int(rtime) % 5 != 0 :
    atime = int(rtime) - (int(rtime) % 5)
    rtime = "%04d" % atime

pathod = "C:\\test"
pathnw = "C:\\test"
#pathnw = "C:\\Users\\彥賢lab\\Desktop\\黑客松\\VDinstance" + "\\" + time.strftime("%Y%m%d")
url = "http://tdata.thb.gov.tw/thbOd/download/vd/five/xml"

if not os.path.isdir(pathnw):      #自動新增資料夾
    os.mkdir(pathnw)
response = requests.get(url)
with open(pathod + "\\" + "vd_value5_" + rtime + ".xml", "wb") as file :
    file.write(response.content)
#urllib.urlretrieve(url, pathod + "\\" + "vd_value_" + time.strftime("%H%M") + ".xml")  #下載VD1檔案

tree = ET.parse(pathod + "\\" + "vd_value5_" + rtime + ".xml")      #讀XML
root = tree.getroot()   #找tree的root位置

Infos_data = open(pathnw + '\\' + "vd_value5_" + rtime + '.csv', 'w', newline='')    #存成CSV   
csvwriter = csv.writer(Infos_data)
Infos_head = []     #attr 名稱
count = 0
count1 = 0
divlevel=0
temp=[]

for member in root[0].findall('Info') :       #從info節點下去找
    divlevel=0
    
    for member1 in member.findall('lane') :     #從 lane節點下去找
        divlevel=divlevel+1
        info = []             #data 內容 , list 格式
        boolin1 = "false"          #vdid 找到後為true
        boolin2 = "false"          #datacollecttime 找到後為true
        boolin3 = "false"          #轉換成 level 後為true
        if count == 0 :
            if count1 == 0 :
                for key, value in member.attrib.items() : 
                    if key == "vdid" :
                        vdid = key

                Infos_head.append(vdid)            #vdid

                nlevel = "level"
                vsrdir="vsrdir"
                Infos_head.append(nlevel)          #level
                Infos_head.append(vsrdir)
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
                if value == "thbVD-21-0130-016-01" : #三灣、南庄
                    vdid = value
                    boolin1 = "true"
                if value == "thbVD-21-0030-105-01" : #獅潭(1)
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
            if key == "vsrdir" :
                vsrdir = value
                boolin2 = "true"
                
            if key == "speed" :
                speed = value
                if int(speed) > 50 :
                    level = 1
                    boolin3 = "true"
                if int(speed) <51 and int(speed) > 30 :
                    level = 2
                    boolin3 = "true"
                if int(speed) < 0 :
                    level = 0
                    boolin3 = "true"        
                if int(speed) < 31 :
                    level = 3
                    boolin3 = "true" 
                 
                    
        info.append(level)
        info.append(vsrdir)

        if boolin1 == "true" and boolin2 == "true" and boolin3 == "true" :    #三個boolin皆為true才存入CSV
            print(info)
            print(divlevel)
            
            if divlevel==1:
                temp.append(level)
                
                if info[0]=="thbVD-21-0130-048-01":
                    print("thbVD-21-0130-048-01===",divlevel)
                    csvwriter.writerow(info) 
                    divlevel=0
                    temp=[]
              
            elif divlevel==2: 
                info[1]=round((info[1]+temp[0])/2,0) 
                temp=[] 
                csvwriter.writerow(info) 
                divlevel=0
            

Infos_data.close()
#os.system("python auto_trans_level.py")