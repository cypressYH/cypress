

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:37:16 2017

@author: 彥賢lab
"""

import pandas as pd
import time



def checkTime(atime) :
    if atime % 100 > 60 :
        atime = atime - 40
    if atime % 100 == 60 :
        atime = atime + 40
    return atime  


def GetNow(returnnow,vd, date,datetime, predicttime,type_x_north,type_x_south) :

    print("in getnow")
    pathist = "C:\\test"  
       
    #探勘即時資料
    ctdatetime = datetime
    print(ctdatetime)
    
    ct = 0
    print(pathist + '\\' + "vd_value5_" + ctdatetime + '.csv')
    while ct < 7 : #8是測試的資料
        try :
            data_file = pd.read_csv(pathist + '\\' + "vd_value5_" + str(ctdatetime) + '.csv', engine = 'python')
            
        except Exception :
            ctdatetime = "%04d"%checkTime(int(ctdatetime)-5)
            continue
        
        line = 0
        file_length = data_file.shape[0]
        
        vdtrue=0
        
        while line < file_length :
 
            if vd == data_file.iloc[line, 0]:
                vdtrue=vdtrue+1
                #預測準確度 

                if data_file.iloc[line, 2]==0: #北
                    type_x_north[ct] = data_file.iloc[line, 1]
                    
                    if vdtrue==2:
                        vdtrue=0
                        break

                if data_file.iloc[line, 2]==1: #南
                    type_x_south[ct] = data_file.iloc[line, 1]
                    
                    if vdtrue==2:
                        vdtrue=0
                        break
   
            line += 1
            
        ctdatetime = "%04d"%checkTime(int(ctdatetime)-5)      
        ct += 1

                
    print("VD設備為 :",vd)
    print("當下時間為 :", datetime)
    print("即時資訊前30分鐘狀態-北 :",type_x_north)
    print("即時資訊前30分鐘狀態-南 :",type_x_south)
    returnnow.append(type_x_north[0]) #回傳現在狀態-北
    returnnow.append(type_x_south[0]) #回傳現在狀態-南
    
    
def GetHistory(vd, data,datetime, predicttime, n_predict, n_mx, type_x,norsou) :    
    k=0
  

    #探勘歷史資料 
    
    if norsou==0: #北
        addnorsou=0

    else:
        addnorsou=1 #南

        
    loop=0
    
    div=0
    if int(datetime)/100>1:
        div=int(int(datetime)/100)
        div=div*24
        ctdatetime = int(datetime)%100
        line=int(((ctdatetime+5)/5)*2)+addnorsou+div   #行數,南要+1
        arrive=int((((int(ctdatetime)+int(predicttime-predicttime%5)))/5)*2)+addnorsou+div #到達時間的行數
        print(">1",line)
        print(arrive)
    
    else:
        ctdatetime = int(datetime)
        line=int(((ctdatetime+5)/5)*2)+addnorsou   #行數,南要+1
        arrive=int((((int(datetime)+int(predicttime-predicttime%5)))/5)*2)+addnorsou #到達時間的行數
     
    data_file = pd.read_csv('show\\historydata\\' + vd  + '.csv', engine = 'python')
    data=[]

    while loop<10:
        data.append([])
        if loop==0:
            data[loop]= data_file.iloc[arrive, :] #到達時間的一整年level資料
        else:
            data[loop]=data_file.iloc[line, :] #5分後,當下,5分前,10分前...的一整年level資料
        line=line-2
        loop=loop+1

   
    i=0
    while i<len(data[0]):

        if data[0][i]==1:  ##歷史資料中到達時間level==1
            n_predict[0]=n_predict[0]+3
            j=0
            
            while j<7:
                k=0
                while k<3:
                    if data[j+k+1][i]==type_x[j]:
                        n_mx[0][j]=n_mx[0][j]+1
                    k=k+1
                j=j+1
                
        if data[0][i]==2:  ##歷史資料中到達時間level==2
            n_predict[1]=n_predict[1]+3
            j=0
            
            while j<7:
                k=0
                while k<3:
                    if data[j+k+1][i]==type_x[j]:
                        n_mx[1][j]=n_mx[1][j]+1
                    k=k+1
                j=j+1   
                
        if data[0][i]==3:  ##歷史資料中到達時間level==3
            n_predict[2]=n_predict[2]+3
            j=0
            
            while j<7:
                k=0
                while k<3:
                    if data[j+k+1][i]==type_x[j]:
                        n_mx[2][j]=n_mx[2][j]+1
                    k=k+1
                j=j+1   
        i=i+1

def Bayes(n_predict,n_mx,returnpredict,norsou): ##貝氏機率
    P_predict_1 = float(n_predict[0]/(n_predict[0]+n_predict[1]+n_predict[2]+21))
    P_predict_2 = float(n_predict[1]/(n_predict[0]+n_predict[1]+n_predict[2]+21))
    P_predict_3 = float(n_predict[2]/(n_predict[0]+n_predict[1]+n_predict[2]+21))

    P_x1_1 = float(n_mx[0][0]/(n_predict[0]))
    P_x1_2 = float(n_mx[1][0]/(n_predict[1]))
    P_x1_3 = float(n_mx[2][0]/(n_predict[2]))
    
    P_x2_1 = float(n_mx[0][1]/(n_predict[0]))
    P_x2_2 = float(n_mx[1][1]/(n_predict[1]))
    P_x2_3 = float(n_mx[2][1]/(n_predict[2]))
    
    P_x3_1 = float(n_mx[0][2]/(n_predict[0]))
    P_x3_2 = float(n_mx[1][2]/(n_predict[1]))
    P_x3_3 = float(n_mx[2][2]/(n_predict[2]))
    
    P_x4_1 = float(n_mx[0][3]/(n_predict[0]))
    P_x4_2 = float(n_mx[1][3]/(n_predict[1]))
    P_x4_3 = float(n_mx[2][3]/(n_predict[2]))
    
    P_x5_1 = float(n_mx[0][4]/(n_predict[0]))
    P_x5_2 = float(n_mx[1][4]/(n_predict[1]))
    P_x5_3 = float(n_mx[2][4]/(n_predict[2]))
    
    P_x6_1 = float(n_mx[0][5]/(n_predict[0]))
    P_x6_2 = float(n_mx[1][5]/(n_predict[1]))
    P_x6_3 = float(n_mx[2][5]/(n_predict[2]))
    
    P_x7_1 = float(n_mx[0][6]/(n_predict[0]))
    P_x7_2 = float(n_mx[1][6]/(n_predict[1]))
    P_x7_3 = float(n_mx[2][6]/(n_predict[2]))

    P_X_1 = float(P_x1_1*P_x2_1*P_x3_1*P_x4_1*P_x5_1*P_x6_1*P_x7_1)
    P_X_2 = float(P_x1_2*P_x2_2*P_x3_2*P_x4_2*P_x5_2*P_x6_2*P_x7_2)
    P_X_3 = float(P_x1_3*P_x2_3*P_x3_3*P_x4_3*P_x5_3*P_x6_3*P_x7_3)
    

    P_1 = (P_X_1*P_predict_1)
    P_2 = (P_X_2*P_predict_2)
    P_3 = (P_X_3*P_predict_3)    
        
    print(n_mx[0][0])
    print(P_predict_1, P_predict_2, P_predict_3)
    print(P_x1_1, P_x2_1, P_x3_1, P_x4_1, P_x5_1, P_x6_1, P_x7_1)
    print(P_x1_2, P_x2_2, P_x3_2, P_x4_2, P_x5_2, P_x6_2, P_x7_2)
    print(P_x1_3, P_x2_3, P_x3_3, P_x4_3, P_x5_3, P_x6_3, P_x7_3)
    print(P_X_1, P_X_2, P_X_3)
    print(P_1, P_2, P_3)
        
    max_P = max(float(P_1), float(P_2), float(P_3))
        
    if max_P == float(P_1) :
        max_T = 1
    elif max_P == float(P_2) :
        max_T = 2
    else :
        max_T = 3
               
        
    str1=''
    #探勘歷史資料 
    
    if norsou==0: #北
        str1='北'
    else: #南
        str1='南'
        
    print(str1+"預測Level :", str(max_T))
    print(str1+"預測機率 :", str(max_P))
    
    returnpredict.append(str(max_T)) #回傳預測level

#self.name, self.vd,self.travellist,self.returnlistt
def topredict(name,vdindex,pre,toreturnlist):
    datetime = time.strftime("%H%M") 

    date = time.strftime("%Y%m%d")
    
    if int(datetime) % 5 != 0 :
        atime = int(datetime) - (int(datetime) % 5)
        datetime = "%04d" % atime    
    
   
    #datetime1="0035"
    #datetime=0
    
    #datetime="%04d"%(int(datetime1)-int(datetime%5))
    print("datetime="+datetime+" date="+date)


    returnlist=[]


    vdarr = ["thbVD-15-0030-036-01", "thbVD-15-0030-041-02", "thbVD-15-0030-047-01", "thbVD-16-0030-071-01", "thbVD-16-0030-077-01",
         "thbVD-16-0030-077-02", "thbVD-16-1180-024-01", "thbVD-21-0030-094-01", "thbVD-21-0130-016-01", "thbVD-21-0030-105-01",
         "thbVD-21-0030-130-01", "thbVD-21-0130-048-01", "thbVD-22-0030-151-01"]


    predicttime=pre[vdindex]
    n_predict = [7,7,7]
    n_mx = [[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]   

    returnnow=[]
    returnpredict=[]

    type_x_north = [0, 0, 0, 0, 0, 0, 0, 0]#第8個為實際結果, 測試用 
    type_x_south = [0, 0, 0, 0, 0, 0, 0 ,0]#第8個為實際結果, 測試用 


    GetNow(toreturnlist[vdindex],vdarr[vdindex], date,datetime, predicttime,type_x_north,type_x_south) #抓取現在時間前30分內的資料
    
    GetHistory(vdarr[vdindex], date,datetime, predicttime, n_predict, n_mx, type_x_north,0) #北的歷史資料
    Bayes(n_predict,n_mx,toreturnlist[vdindex],0)

    print(n_predict)
    print(n_mx)

    n_predict = [7,7,7]
    n_mx = [[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]   


    GetHistory(vdarr[vdindex], date,datetime, predicttime, n_predict, n_mx, type_x_south,1)#南的歷史資料
    Bayes(n_predict,n_mx,toreturnlist[vdindex],1)

    print(n_predict)
    print(n_mx)

    print("name=",name,"toreturnlistt=",toreturnlist[vdindex])




    

    
