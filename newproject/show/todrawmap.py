# -*- coding: utf-8 -*-
import gmplot
from django.shortcuts import render
from django.template import Context, loader
import re
import json
from urllib.request import urlopen


def getip():  #抓取使用者目前ip
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    userloc=data['loc']
    
    print(IP)  
    print(userloc)

    
def todrawarrow(lat,lng,nor,sou,vd,gmap):

        
    if vd==0:
    #大溪
        npoint1=[24.889065, 121.299428]
        npoint2=[24.88452,121.29035]
        npoint3=[24.887119, 121.297625]
        npoint4=[24.889065, 121.295823]
        
        spoint1=[24.889688, 121.282176]
        spoint2=[24.88452,121.29035]
        spoint3=[24.889922, 121.285094]
        spoint4=[24.887586, 121.283120]
 
    if vd==1:
    #平鎮
        npoint1=[24.896309, 121.277823]
        npoint2=[24.88848,121.26997]
        npoint3=[24.892319, 121.276232]
        npoint4=[24.895206, 121.273986]
        
        spoint1=[24.880092, 121.262380]
        spoint2=[24.88848,121.26997]
        spoint3=[24.883998, 121.263596]
        spoint4=[24.882130, 121.266217]

    if vd==2:
    #龍潭
        npoint1=[24.874267, 121.234013]
        npoint2=[24.87034,121.22307]
        npoint3=[24.874437, 121.229426]
        npoint4=[24.871210, 121.230924]
        
        spoint1=[24.865436, 121.212391]
        spoint2=[24.87034,121.22307]
        spoint3=[24.868833, 121.215199]
        spoint4=[24.865945, 121.217071]
        
    if vd==3:
    #橫山
        npoint1=[24.716615, 121.143691]
        npoint2=[24.72307,121.13471]
        npoint3=[24.720186, 121.141444]
        npoint4=[24.717465, 121.139198]
        
        spoint1=[24.728603, 121.124316]
        spoint2=[24.72307,121.13471]
        spoint3=[24.728518, 121.128996]
        spoint4=[24.725372, 121.127030]
   
    if vd==4:
    #竹東
        npoint1=[24.728756, 121.089601]
        npoint2=[24.72341,121.07922]
        npoint3=[24.725441, 121.086793]
        npoint4=[24.728501, 121.085202]
        
        spoint1=[24.713708, 121.073970]
        spoint2=[24.72341,121.07922]
        spoint3=[24.716428, 121.077433]
        spoint4=[24.718044, 121.073970]

    if vd==5:
    #北埔
        npoint1=[24.729803, 121.081259]
        npoint2=[24.72093,121.07508]
        npoint3=[24.725807, 121.080698]
        npoint4=[24.727592, 121.077703]
        
        spoint1=[24.711438, 121.069092]
        spoint2=[24.72093,121.07508]
        spoint3=[24.713904, 121.072648]
        spoint4=[24.715519, 121.069466]

    if vd==6:
    #關西
        npoint1=[24.805536, 121.159631]
        npoint2=[24.79864,121.16910]
        npoint3=[24.801967, 121.161597]
        npoint4=[24.804516, 121.164030]
        
        spoint1=[24.792706, 121.178257]
        spoint2=[24.79864,121.16910]
        spoint3=[24.793300, 121.173764]
        spoint4=[24.796189, 121.176011]        
        
    if vd==7:
    #峨嵋、頭份
        npoint1=[24.686127, 120.963203]
        npoint2=[24.67569,120.96589]
        npoint3=[24.682215, 120.962173]
        npoint4=[24.683235, 120.966104]
        
        spoint1=[24.664949, 120.965168]
        spoint2=[24.67569,120.96589]
        spoint3=[24.668606, 120.967227]
        spoint4=[24.668776, 120.963483]        
        
    if vd==8:
    #三灣
        npoint1=[24.656065, 120.962617]
        npoint2=[24.64881,120.95441]
        npoint3=[24.654619, 120.958405]
        npoint4=[24.652237, 120.961025]
        
        spoint1=[24.637860, 120.955597]
        spoint2=[24.64881,120.95441]
        spoint3=[24.642029, 120.956813]
        spoint4=[24.641348, 120.953069]        
    if vd==9:
    #獅潭、南庄
        npoint1=[24.612411, 120.959772]
        npoint2=[24.60186,120.95814]
        npoint3=[24.608411, 120.961457]
        npoint4=[24.608751, 120.957432]
        
        spoint1=[24.592667, 120.952846]
        spoint2=[24.60186,120.95814]
        spoint3=[24.596752, 120.952940]
        spoint4=[24.595390, 120.956403]        
    if vd==10:
    #太湖
        npoint1=[24.440029, 120.872302]
        npoint2=[24.42992,120.86835]
        npoint3=[24.436620, 120.869213]
        npoint4=[24.435853, 120.872770]
        
        spoint1=[24.420002, 120.863504]
        spoint2=[24.42992,120.86835]
        spoint3=[24.422985, 120.866686]
        spoint4=[24.424434, 120.863223]        
        
    if vd==11:
    #三義
        npoint1=[24.421014, 120.775128]
        npoint2=[24.41150,120.76914]
        npoint3=[24.416753, 120.774566]
        npoint4=[24.418628, 120.771290]
        
        spoint1=[24.402178, 120.763615]
        spoint2=[24.41150,120.76914]
        spoint3=[24.406355, 120.763709]
        spoint4=[24.404735, 120.767078]        
        
    if vd==12:
    #卓蘭
        npoint1=[24.310369, 120.797228]
        npoint2=[24.30042,120.8021]
        npoint3=[24.307554, 120.800410]
        npoint4=[24.306190, 120.797134]
        
        spoint1=[24.290066, 120.801346]
        spoint2=[24.30042,120.8021]
        spoint3=[24.293223, 120.803125]
        spoint4=[24.293564, 120.799381]        


    nline1lat=[npoint1[0],npoint2[0]]
    nline1lng=[npoint1[1],npoint2[1]]
    nline2lat=[npoint1[0],npoint4[0]]
    nline2lng=[npoint1[1],npoint4[1]]
    nline3lat=[npoint1[0],npoint3[0]]
    nline3lng=[npoint1[1],npoint3[1]]
        
    sline1lat=[spoint1[0],spoint2[0]]
    sline1lng=[spoint1[1],spoint2[1]]
    sline2lat=[spoint1[0],spoint4[0]]
    sline2lng=[spoint1[1],spoint4[1]]
    sline3lat=[spoint1[0],spoint3[0]]
    sline3lng=[spoint1[1],spoint3[1]]

    gmap.plot(nline1lat,nline1lng,nor, edge_width=5)   #畫北上的箭頭    
    gmap.plot(nline2lat,nline2lng,nor, edge_width=5)   
    gmap.plot(nline3lat,nline3lng,nor, edge_width=5)

    gmap.plot(sline1lat,sline1lng,sou, edge_width=5)    #畫南下的箭頭       
    gmap.plot(sline2lat,sline2lng,sou, edge_width=5)   
    gmap.plot(sline3lat,sline3lng,sou, edge_width=5)
    

def todrawmap(predictlist,travellist):
    print("in todrawmap")
    
    gmap = gmplot.GoogleMapPlotter(24.799510,120.979011, 12)
    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

   
    lat=[24.88452,24.88848,24.87034,24.72307,24.72341,24.72093,24.79864,24.67569,24.64881,24.60186,24.42992,24.41150,24.30042]
    lng=[121.29035,121.26997,121.22307,121.13471,121.07922,121.07508,121.16910,120.96589,120.95441,120.95814,120.86835,120.76914,120.8021]


    name=["大溪","平鎮","龍潭","橫山","竹東","北埔","關西","峨嵋and頭份","三灣","獅潭and南庄","太湖","三義","卓蘭"]
    

    gmap.marker(24.799510,120.979011,'red', title="your location")
    
    print("toreturnlist=",predictlist)
    
    #現在狀態
    j=0
    while j<13:
        slevel=''
        nlevel=''
        
        if int(predictlist[j][2])==3:  #預測北
            nlevel='jamed'
            norc='red'
            
        elif int(predictlist[j][2])==2:
            nlevel='crowded'
            norc='orange'
            
        else:
            nlevel='smooth'
            norc='green'
            
            
        if int(predictlist[j][3])==3:  #預測南
            slevel='jamed'
            souc='red'
            
        elif int(predictlist[j][3])==2:
            slevel='crowded'
            souc='orange'
            
        else:
            slevel='smooth'
            souc='green'
            
            
        snlevel=''
        nnlevel=''
        if int(predictlist[j][0])==3:  #現在北
            nnlevel='jamed'
            nnorc='red'
            
        elif int(predictlist[j][0])==2:
            nnlevel='crowded'
            nnorc='orange'
            
        else:
            nnlevel='smooth'
            nnorc='green'
            
            
        if int(predictlist[j][1])==3:  #現在南
            snlevel='jamed'
            snouc='red'
            
        elif int(predictlist[j][1])==2:
            snlevel='crowded'
            snouc='orange'
            
        else:
            snlevel='smooth'
            snouc='green'    
            
        strinfo="Arrive in "+str(travellist[j])+" minute. Now: Northbound lane is "+nnlevel+".Southbound lane is "+snlevel+". After "+str(travellist[j])+" minute: Northbound lane will be "+nlevel+". Southbound lane will be "+slevel
        gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
        print(slevel)
        gmap.marker(lat[j],lng[j],'blue', title=strinfo)  #告知現在跟預測LEVEL
        todrawarrow(lat[j],lng[j],norc,souc,j,gmap) #畫箭頭
        j=j+1

    
    gmap.draw("show/templates/mymap.html")  #產生地圖網頁

