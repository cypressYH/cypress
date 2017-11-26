# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:37:16 2017

@author: 彥賢lab
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from show.todrawmap import todrawmap
from show.traveltime import traveltime
from show.mypredict import topredict
import sys
import threading

class myThread (threading.Thread):
    def __init__(self, threadID, name,vd,travellist ,returnlistt):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.vd = vd
        self.travellist=travellist
        self.returnlistt=returnlistt
    def run(self):
        print ("開始：" + self.name)
        topredict(self.name, self.vd,self.travellist,self.returnlistt)
        print ("退出：" + self.name)


def index(request):
    
    print("sys.getdefaultencoding()"+sys.getdefaultencoding())

    #抓取到達景點的時間
    travellist=traveltime()
    
    ##畫地圖(預測level,到達時間)
    
    returnlistt=[]
    i=0
    while i<13:
        returnlistt.append([])
        i=i+1
    
    thread0 = myThread(1, "Thread-1",0,travellist ,returnlistt)
    thread1 = myThread(2, "Thread-2",1,travellist,returnlistt)
    thread2 = myThread(3, "Thread-3",2,travellist,returnlistt)
    thread3 = myThread(4, "Thread-4",3,travellist,returnlistt)
    thread4 = myThread(5, "Thread-5",4,travellist,returnlistt)
    thread5 = myThread(6, "Thread-6",5,travellist,returnlistt)
    thread6 = myThread(7, "Thread-7",6,travellist,returnlistt)
    thread7 = myThread(8, "Thread-8",7,travellist,returnlistt)
    thread8 = myThread(9, "Thread-9",8,travellist,returnlistt)
    thread9 = myThread(10, "Thread-10",9,travellist,returnlistt)
    thread10 = myThread(11, "Thread-11",10,travellist,returnlistt)
    thread11 = myThread(12, "Thread-12",11,travellist,returnlistt)
    thread12 = myThread(13, "Thread-13",12,travellist,returnlistt)
    
    thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    
    thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    thread12.join()
    
    
    todrawmap(returnlistt,travellist)
    template = loader.get_template("mymap.html")
    

    return HttpResponse(template.render())
