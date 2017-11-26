# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:37:16 2017

@author: 彥賢lab
"""
import urllib.request
import simplejson as json
from django.contrib.gis.geoip2 import GeoIP2
import re
import json
from urllib.request import urlopen
import time


def traveltime():

    url = 'http://ipinfo.io/json' #抓取使用者ip
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    userloc=data['loc']

    
    destination ="24.88452,121.29035|24.88848,121.26997|24.87034,121.22307|24.72307,121.13471|24.72341,121.07922|24.72093,121.07508|24.79864,121.16910|24.67569,120.96589|24.64881,120.95441|24.60186,120.95814|24.42992,120.86835|24.41150,120.76914|24.30042,120.8021"
##目的:大溪|平鎮|龍潭|橫山|竹東|北埔|關西|峨嵋、頭份|三灣|獅潭、南庄|太湖|三義|卓蘭

    ##用來儲存旅行時間的list，單位為分鐘
    listduration=[]

    ##用http詢問google map旅行時間
    torequestgoogle=urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=24.799510,120.979011&destinations="+destination).read()


    jsonResponse = json.loads(torequestgoogle.decode('utf-8'))

    for elements in jsonResponse['rows'][0]['elements']:
        duration=elements['duration']['value']
        listduration.append(int(duration/60))
        
    print("in traveltime listduration")
    print(listduration)
    
    return listduration
