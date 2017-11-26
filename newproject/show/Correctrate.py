# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:37:16 2017

@author: 彥賢lab
"""

import pandas as pd
import csv
import random 



def checkTime(atime) :
    if atime % 100 > 60 :
        atime = atime - 40
    if atime % 100 == 60 :
        atime = atime + 40
    return atime  


def GetNow(vd, data,datetime, predicttime,  type_x,norsou) :    


    #從歷史資料探勘預測式的資料 
    
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
        line=int(((ctdatetime)/5)*2)+addnorsou+div   #行數,南要+1
        arrive=int((((int(ctdatetime)+int(predicttime-predicttime%5)))/5)*2)+addnorsou+div #到達時間的行數
    
    else:
        ctdatetime = int(datetime)
        line=int(((ctdatetime)/5)*2)+addnorsou   #行數,南要+1
        arrive=int((((int(datetime)+int(predicttime-predicttime%5)))/5)*2)+addnorsou #到達時間的行數
        
        
    data_file = pd.read_csv('historydata\\' + vd  + '.csv', engine = 'python')

    #data.append([])
    

    thisline=data_file[date]


    
    while loop<8:


        if loop==7:
            type_x.append(thisline[arrive]) #到達時間的當天的level資料
                
        else:
            type_x.append(thisline[line]) #當下,5分前,10分前...當天的level資料
        line=line-2
        loop=loop+1


    
    
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

    
    else:
        ctdatetime = int(datetime)
        line=int(((ctdatetime+5)/5)*2)+addnorsou   #行數,南要+1
        arrive=int((((int(datetime)+int(predicttime-predicttime%5)))/5)*2)+addnorsou #到達時間的行數

     
    data_file = pd.read_csv('historydata\\' + vd  + '.csv', engine = 'python')
    data=[]
    #data.append([])

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

        if data[0][i]==1:  ##到達時間level==1
            n_predict[0]=n_predict[0]+3
            j=0
            
            while j<7:
                k=0
                while k<3:
                    if data[j+k+1][i]==type_x[j]:
                        n_mx[0][j]=n_mx[0][j]+1
                    k=k+1
                j=j+1
                
        if data[0][i]==2:  ##到達時間level==2
            n_predict[1]=n_predict[1]+3
            j=0
            
            while j<7:
                k=0
                while k<3:
                    if data[j+k+1][i]==type_x[j]:
                        n_mx[1][j]=n_mx[1][j]+1
                    k=k+1
                j=j+1   
                
        if data[0][i]==3:  ##到達時間level==3
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

def Bayes(n_predict,n_mx,returnpredict,norsou):
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
    
    #P_1 = "%.5f"%(P_X_1*P_predict_1)
    #P_2 = "%.5f"%(P_X_2*P_predict_2)
    #P_3 = "%.5f"%(P_X_3*P_predict_3)
    
    P_1 = (P_X_1*P_predict_1)
    P_2 = (P_X_2*P_predict_2)
    P_3 = (P_X_3*P_predict_3)    
        
    #print(n_mx[0][0])
    #print(P_predict_1, P_predict_2, P_predict_3)
    #print(P_x1_1, P_x2_1, P_x3_1, P_x4_1, P_x5_1, P_x6_1, P_x7_1)
    #print(P_x1_2, P_x2_2, P_x3_2, P_x4_2, P_x5_2, P_x6_2, P_x7_2)
    #print(P_x1_3, P_x2_3, P_x3_3, P_x4_3, P_x5_3, P_x6_3, P_x7_3)
    #print(P_X_1, P_X_2, P_X_3)
    #print(P_1, P_2, P_3)
        
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
    
    returnpredict.append(str(max_T))


def main(date,datetime1):
#datetime = time.strftime("%H%M") 


    datetime=0
    
    datetime="%04d"%(int(datetime1)-int(datetime1)%5)
    print("datetime"+datetime)
    
    #predicttime=15 
    pret = [15, 15, 20, 23, 28,
        30, 31, 40, 48,50, 57,
        66, 69]

    returnlist=[]


    vdarr = ["thbVD-15-0030-036-01", "thbVD-15-0030-041-02", "thbVD-15-0030-047-01", "thbVD-16-0030-071-01", "thbVD-16-0030-077-01",
         "thbVD-16-0030-077-02", "thbVD-16-1180-024-01", "thbVD-21-0030-094-01", "thbVD-21-0130-016-01", "thbVD-21-0030-105-01",
         "thbVD-21-0030-130-01", "thbVD-21-0130-048-01", "thbVD-22-0030-151-01"]
    i=0

    while i<13:


        n_predict = [7,7,7]
        n_mx = [[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]   

        returnnow=[]
        returnpredict=[]

        type_x_north = []#第8個為實際結果, 測試用 
        type_x_south = []#第8個為實際結果, 測試用 


        GetNow(vdarr[i], date,datetime, pret[i],type_x_north,0)
        GetHistory(vdarr[i], date,datetime, pret[i], n_predict, n_mx, type_x_north,0) #北的歷史資料
        Bayes(n_predict,n_mx,returnpredict,0)



        n_predict = [7,7,7]
        n_mx = [[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]   

        GetNow(vdarr[i], date,datetime, pret[i],type_x_south,1)
        GetHistory(vdarr[i], date,datetime, pret[i], n_predict, n_mx, type_x_south,1)#南的歷史資料
        Bayes(n_predict,n_mx,returnpredict,1)



        print("VD設備為 :",vdarr[i])
        print("當下時間為 :", datetime)
        print("即時資訊前30分鐘狀態-北 :",type_x_north)
        print("即時資訊前30分鐘狀態-南 :",type_x_south)
        returnnow.append(type_x_north[7])
        returnnow.append(type_x_south[7])

        returnlist.append(returnnow)### 正確的level
        returnlist.append(returnpredict)###預測的level



        path2 = "C:\\Users\\user\\newproject\\newproject\\show\\準確度"      
    

        rightt=[]
        
        with open(path2 + '\\' +vdarr[i]+ '準確度.csv', 'a+', newline='') as Infos_data2:   #存成CSV  
            csvwriter2 = csv.writer(Infos_data2)
            

            
            if int(type_x_north[7])==int(returnpredict[0]):
                rightt.append(1)

                
                
            if int(type_x_north[7])!=int(returnpredict[0]):
                rightt.append(0)

            
            if int(type_x_south[7])==int(returnpredict[1]):
                rightt.append(1)

                
            if int(type_x_south[7])!=int(returnpredict[1]):
                rightt.append(0)           
  
                
            rightt.append(date)
            rightt.append(datetime1)
            
            csvwriter2.writerow(rightt)
            Infos_data2.close()
            
        i=i+1
        

    rightnorth=0
    rightsouth=0
    info=[]
    
    path2 = "C:\\Users\\user\\newproject\\newproject\\show\\"      
    
    #Infos_data = open(path2 + '\\' + '準確度.csv', 'a+', newline='')    #存成CSV  
    #csvwriter = csv.writer(Infos_data)
    with open(path2 + '\\' + '準確度.csv', 'a+', newline='') as Infos_data:   #存成CSV  
        csvwriter = csv.writer(Infos_data)
    
    
        k=0
        while k<26:
            
            if returnlist[k][0]==int(returnlist[k+1][0]):
                rightnorth+=1

        
            if returnlist[k][1]==int(returnlist[k+1][1]):
                rightsouth+=1    

            k+=2
       

    
        print(float(rightnorth/13))
        print(float(rightsouth/13))
    
        info.append(float(rightnorth/13))
        info.append(float(rightsouth/13))

        info.append(date)
        info.append(datetime1)
        
    
        print(info)
        csvwriter.writerow(info)

        Infos_data.close()
        



 
    
    return returnlist    
    
i=0
while i<22:
    
    date = str(20171101+i)
    hour=0
    print("==================下一天:",date,"=====================")
    
    while hour<15:
        print("==================下個小時:",hour,"===================")
        datetime1=str("%02d" %(8+hour)+"%02d"%(random.randint(1,50)))
        main(date,datetime1)
        hour+=1
    
    
    i=i+1
