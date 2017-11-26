# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:27:00 2017

@author: 彥賢lab
"""

import pandas as pd
import numpy as np
from itertools import zip_longest
import csv

def checkDicDate(dirdig) :
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
    return dirdig

def addValueToMat(theMat, key, value, incr):
    if key not in theMat :
        theMat[key] = dict()
        theMat[key][value] = incr
    else :
        if value not in theMat[key]:
            theMat[key][value] = incr
        else :
            theMat[key][value] += incr
        
def addMat(theMat, key, value) :
    if key not in theMat :
        theMat[key] = value
    else :
        theMat[key] = value 

def InitStat() :
    odate = 20171123
    path = "C:\\Users\\mis\\Desktop\\hackerthon\\data"
    pathnw = "C:\\Users\\mis\\Desktop\\hackerthon\\"
    # VD 設備的 ID
    vdarr = ["thbVD-15-0030-036-01", "thbVD-15-0030-041-02", "thbVD-15-0030-047-01", "thbVD-16-0030-071-01", "thbVD-16-0030-077-01",
             "thbVD-16-0030-077-02", "thbVD-16-1180-024-01", "thbVD-21-0030-094-01", "thbVD-21-0130-016-01", "thbVD-21-0030-105-01",
             "thbVD-21-0030-130-01", "thbVD-21-0130-048-01", "thbVD-22-0030-151-01"]
    
    Infos_data1 = open(pathnw + vdarr[0] + '.csv', 'wt', newline='')    #存成CSV  
    Infos_data2 = open(pathnw + vdarr[1] + '.csv', 'wt', newline='')
    Infos_data3 = open(pathnw + vdarr[2] + '.csv', 'wt', newline='')
    Infos_data4 = open(pathnw + vdarr[3] + '.csv', 'wt', newline='')
    Infos_data5 = open(pathnw + vdarr[4] + '.csv', 'wt', newline='')
    Infos_data6 = open(pathnw + vdarr[5] + '.csv', 'wt', newline='')
    Infos_data7 = open(pathnw + vdarr[6] + '.csv', 'wt', newline='')
    Infos_data8 = open(pathnw + vdarr[7] + '.csv', 'wt', newline='')
    Infos_data9 = open(pathnw + vdarr[8] + '.csv', 'wt', newline='')
    Infos_data10 = open(pathnw + vdarr[9] + '.csv', 'wt', newline='')
    Infos_data11 = open(pathnw + vdarr[10] + '.csv', 'wt', newline='')
    Infos_data12 = open(pathnw + vdarr[11] + '.csv', 'wt', newline='')
    Infos_data13 = open(pathnw + vdarr[12] + '.csv', 'wt', newline='') 

    Infos_head1 = []     #attr 名稱
    Infos_head2 = []
    Infos_head3 = []
    Infos_head4 = []
    Infos_head5 = []
    Infos_head6 = []
    Infos_head7 = []
    Infos_head8 = []
    Infos_head9 = []
    Infos_head10 = []
    Infos_head11 = []
    Infos_head12 = []
    Infos_head13 = []
    #20161001 - 20171122 共 418個
    arr = [np.zeros((3, 576), int), np.zeros((3, 576), int), np.zeros((3, 576), int), np.zeros((3, 576), int),
           np.zeros((3, 576), int), np.zeros((3, 576), int), np.zeros((3, 576), int), np.zeros((3, 576), int),
           np.zeros((3, 576), int), np.zeros((3, 576), int), np.zeros((3, 576), int), np.zeros((3, 576), int),
           np.zeros((3, 576), int)]
    
    ckindex = 0
    while odate < 20171126 :
        print(str(odate))
        Infos_head1.append(odate)     #attr 名稱
        Infos_head2.append(odate)
        Infos_head3.append(odate)
        Infos_head4.append(odate)
        Infos_head5.append(odate)
        Infos_head6.append(odate)
        Infos_head7.append(odate)
        Infos_head8.append(odate)
        Infos_head9.append(odate)
        Infos_head10.append(odate)
        Infos_head11.append(odate)
        Infos_head12.append(odate)
        Infos_head13.append(odate)
        
        namenum = 0
        ct = 0
        while  namenum < 2360:        #以秒為單位
            #print(str(namenum))
            dirname = "vd_value5_" + "%04d" % namenum       #檔名
            try :
                data_file = pd.read_csv(path + '\\' + str(odate) + '\\' + dirname + '.csv', engine = 'python')
            except Exception : 
                ct += 5
                namenum += 5
                if ct == 60 :   #60秒
                    ct = 0
                    namenum += 40
                continue
            line = 0
            file_length = data_file.shape[0]
            while line < file_length :
                for vd in vdarr :
                    if vd == data_file.iloc[line, 0]:
                        if data_file.iloc[line, 2] == 0:
                            arr[vdarr.index(vd)][ckindex][2*(int(namenum/100)*12+int((namenum%100)/5))] += data_file.iloc[line, 1]
                            #print(vdarr.index(vd), ckindex, 2*(int(namenum/100)*12+int((namenum%100)/5)), data_file.iloc[line, 1])
                        else :
                            arr[vdarr.index(vd)][ckindex][2*(int(namenum/100)*12+int((namenum%100)/5))+1] += data_file.iloc[line, 1]
                            #print(vdarr.index(vd), ckindex, 2*(int(namenum/100)*12+int((namenum%100)/5))+1, data_file.iloc[line, 1])
                line += 1
            ct += 5
            namenum += 5
            if ct == 60:
                ct = 0
                namenum += 40                
        ckindex += 1
        odate = checkDicDate(odate + 1)        
    func2 = lambda x: np.around(x/2)
    for i in range(0, 13):
        if i != 11 :
            arr[i] = map(func2, arr[i])

    csvwriter1 = csv.writer(Infos_data1)
    csvwriter1.writerow(Infos_head1)
    csvwriter2 = csv.writer(Infos_data2)
    csvwriter2.writerow(Infos_head2)
    csvwriter3 = csv.writer(Infos_data3)
    csvwriter3.writerow(Infos_head3)
    csvwriter4 = csv.writer(Infos_data4)
    csvwriter4.writerow(Infos_head4)
    csvwriter5 = csv.writer(Infos_data5)
    csvwriter5.writerow(Infos_head5)
    csvwriter6 = csv.writer(Infos_data6)
    csvwriter6.writerow(Infos_head6)
    csvwriter7 = csv.writer(Infos_data7)
    csvwriter7.writerow(Infos_head7)
    csvwriter8 = csv.writer(Infos_data8)
    csvwriter8.writerow(Infos_head8)
    csvwriter9 = csv.writer(Infos_data9)
    csvwriter9.writerow(Infos_head9)
    csvwriter10 = csv.writer(Infos_data10)
    csvwriter10.writerow(Infos_head10)
    csvwriter11 = csv.writer(Infos_data11)
    csvwriter11.writerow(Infos_head11)
    csvwriter12 = csv.writer(Infos_data12)
    csvwriter12.writerow(Infos_head12)
    csvwriter13 = csv.writer(Infos_data13)
    csvwriter13.writerow(Infos_head13)            
        
    export_data1 = zip_longest(*arr[0], fillvalue = '')   #轉陣列
    export_data2 = zip_longest(*arr[1], fillvalue = '')
    export_data3 = zip_longest(*arr[2], fillvalue = '')
    export_data4 = zip_longest(*arr[3], fillvalue = '')
    export_data5 = zip_longest(*arr[4], fillvalue = '')
    export_data6 = zip_longest(*arr[5], fillvalue = '')
    export_data7 = zip_longest(*arr[6], fillvalue = '')
    export_data8 = zip_longest(*arr[7], fillvalue = '')
    export_data9 = zip_longest(*arr[8], fillvalue = '')
    export_data10 = zip_longest(*arr[9], fillvalue = '')
    export_data11 = zip_longest(*arr[10], fillvalue = '')
    export_data12 = zip_longest(*arr[11], fillvalue = '')
    export_data13 = zip_longest(*arr[12], fillvalue = '')
    
    csvwriter1.writerows(export_data1)
    csvwriter2.writerows(export_data2)
    csvwriter3.writerows(export_data3)
    csvwriter4.writerows(export_data4)
    csvwriter5.writerows(export_data5)
    csvwriter6.writerows(export_data6)
    csvwriter7.writerows(export_data7)
    csvwriter8.writerows(export_data8)
    csvwriter9.writerows(export_data9)
    csvwriter10.writerows(export_data10)
    csvwriter11.writerows(export_data11)
    csvwriter12.writerows(export_data12)
    csvwriter13.writerows(export_data13)     
  
    Infos_data1.close()
    Infos_data2.close()
    Infos_data3.close()
    Infos_data4.close()
    Infos_data5.close()
    Infos_data6.close()
    Infos_data7.close()
    Infos_data8.close()
    Infos_data9.close()
    Infos_data10.close()
    Infos_data11.close()
    Infos_data12.close()
    Infos_data13.close()
 
InitStat()