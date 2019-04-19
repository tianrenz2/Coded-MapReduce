#This program is for generalized coded MapReduce
#The amount of user is variable.
#number of files is 12
#First part is for the procedure code
#Second part is creating files
#Third part is mapping
#Fourth part is shuffle

############### Part 1  ##################
############ Procedure Code ##############

################ Naming ##################
'''
Users:n
replicant: r
copy:c [original is garmar]
file naming: Alpha_beta_gammar_delta
Alpha and beta: where the file exist which means r=2
delta=number of users=n
'''
'''
******* PART 1 FILE CREATING
Procedure
    n=random integer
    for value1 =< n and value 2 =< n do
        create filename
        create random integer and write in the file
    end for
end procedure

******* PART 2 MAP TASKS
proceduer
    for n folder create
        copy value1_value2 into the foler value1 or value2
    end for
end procedure

******* PART 3 SHUFFLING
PROCEDURE
    for n multi-processing do
    temp=[]
    #set current folder value=alpha
    calculate S1=n-alpha
        for value1 in S1
            calculate S2=S1-value1
            for value2 in S2
            
            if value1>alpha: #this step is trying to match the file name under the current user folder
                alpha_value1_1_value2
            else:
                value1_alpha_2_value2
            if value2 >alpha:
                alpha_value2_1_value1
            else:
                value2_alpha_2_value1
                temp.append
            end for
        end for
    #in temp file should have 6 file while having 4 users
    choose two do the combination, check two file's value1=value2
    send the file two both user1 and user 2
    end for
PROCEDURE


******* PART 4 DECODING
procedure
    for n multi-processing do
        if file1a.exist
            file3ab-file1a=file2b
        else do
            file3ab-file2b=file1a
        end if
    end for
end procedure

thinking flowchart will be easier, first time do psedo code may not be good enough
PS：original pseudo code is based on super machine,more fit for weiqi's design
I made change for the shuffling. The result should be same.

'''
############### Part 2  ##################
############ Creating Files ##############
import timeit
import sys
import os
#import numpy as np
#import pandas as pd
#import dispy
import shutil
import re
import time
import threading#, Queue
import random
import math
#from multiprocessing import Process,Lock,Pool
import time,datetime
import multiprocessing

def filecreator():
####finish created director
    for i in range(users):
        for j in range(users):
            for k in range(2):
                for l in range(users):
                    if i != j and i<j:
                        filename=str(i+1)+"_"+str(j+1)+"_"+str(k+1)+"_"+str(l+1)+".txt"
                        filegen=open(filename,'w')
                        generate = str(random.randint(0,9000))
                        #sys.stdout= open(filename,'w')#create a txt file
                        filegen.write(generate) #store all the numbers which generate earier to the txt  file
                        filegen.close()
                        #sys.stdout.close()


############### Part 3  ##################
############# Mapping Code  ##############
def Mapping():
    files= os.listdir(folder_path) #get file name under the folder
    results = set() #find folder name
    number_result=set()
    for files_names in files:
        files_name=files_names.split('.')
        file_name=files_name[0].split('_')
        if len(files_names) > 4:
            first = "coded_"+file_name[0]
            third = "coded_"+file_name[1]
            results.add(first)
            results.add(third)
            number_first=file_name[0]
            number_third=file_name[1]
            number_result.add(number_first)
            number_result.add(number_third)
    results=list(results)
    number_result=list(number_result)
    #print(number_result)
    os.chdir(path)#change the director for the folder path
    #print(results)
    for folder_name in results:#delete folders that exists from previous run
        if os.path.exists(path):
            #print(folder_name)
            shutil.rmtree(folder_name)

    for folder_name in results:#create new folders for the number desired
        if os.path.isdir(path):
            os.mkdir(os.path.join(path, folder_name))
            new_path=path+'/'+folder_name
            if os.path.isdir(path):
                os.mkdir(os.path.join(new_path, folder_name))
    counter=0
    
    for files_names in files:
        files_name=files_names.split('.')
        file_name=files_name[0].split('_')
        if len(files_names) > 4:
            first="coded_"+file_name[0]
            third="coded_"+file_name[1]
            shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_master/'+files_names, '/Users/xiaoran/dropbox/cache_map/'+first)
            shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_master/'+files_names, '/Users/xiaoran/dropbox/cache_map/'+third)
                #print(results)
    #print(number_result)
#print(type(file_name))

    return (results,number_result)
############### Part 41 ##################
##### Shuffling Code for generate ########
def shufgen(val1):
    L1=val1
    L2=L1[:]
    L3=[] #除去两个随机
    L4=[] #
    L5=[]
    L6=[]
    D1={}
    temp=[]
    #print(L1)
    for i in range(len(L1)):
        L2.pop(i)
        L2=random.sample(L2,len(L2))
        D1[L1[i]]=L2
        L2=L1[:]
    #print(D1)
    for key,value in D1.items():
        temp=value[:]
        #print("for user #"+str(key))
        for i in range(len(temp)):
            a=temp.pop(i)
            temp=random.sample(temp,len(temp))
            for j in range(len(temp)):
                if [key,a,temp[j]] not in L4 and [key,temp[j],a] not in L4:
                    L4.append([key,a,temp[j]])
            #print(L4)
            temp=value[:]
        L4=random.sample(L4,len(L4))
#L4.insert(0,key)
        L5.append([key,L4])
#print(*L4,sep = '\n')
        L4=[]
#print(L3)
#print(L3)
    return L5
############### Part 4  ##################
############ Shuffling Code ##############
#print (results)
def Encoding(val1):
    jeffdean1=val1
    #print(jeffdean1)
    foldervalue=jeffdean1[0]
    jeffdeanlist=jeffdean1[1]
    #for new_folder_name in results:#create new file in different folder
    path_folder="/Users/xiaoran/dropbox/cache_map/coded_"+jeffdean1[0]
    # print(path_folder)
    os.chdir(path_folder)
    #print(jeffdeanlist)
    print("current running" + jeffdean1[0])
    folder_naming=[]
    #print("jeffdean len", len(jeffdeanlist))
    for index, i in enumerate(jeffdeanlist):
        value1=i[1]
        value2=i[2]
        #print("jeff dean list: ",index ,str(i))
        name = []
        #print(value1,value2)
#        print("jeffdean Item",i,value1,value2)
        if value1 > foldervalue:
            file1=foldervalue+"_"+value1+"_1_"+value2
            with open("/Users/xiaoran/dropbox/cache_map/coded_"+jeffdean1[0]+"/"+foldervalue+"_"+value1+"_1_"+value2+".txt",'r') as f1:
                name.append(file1)
                a=int(f1.read())
        else:
            file1=value1+"_"+foldervalue+"_2_"+value2
            with open("/Users/xiaoran/dropbox/cache_map/coded_"+jeffdean1[0]+"/"+value1+"_"+foldervalue+"_2_"+value2+".txt",'r') as f1:
                name.append(file1)
                a=int(f1.read())
        if value2 > foldervalue:
            file2=foldervalue+"_"+value2+"_1_"+value1
            with open("/Users/xiaoran/dropbox/cache_map/coded_"+jeffdean1[0]+"/"+foldervalue+"_"+value2+"_1_"+value1+".txt",'r') as f2:
                name.append(file2)
                b=int(f2.read())
        else:
            file2=value2+"_"+foldervalue+"_2_"+value1
            with open("/Users/xiaoran/dropbox/cache_map/coded_"+jeffdean1[0]+"/"+value2+"_"+foldervalue+"_2_"+value1+".txt",'r') as f2:
                name.append(file2)
                b=int(f2.read())
        total=str(a+b)
        if value1 >value2:
            transfer2=str(name[1]+'__'+name[0])
        else:
            transfer2=str(name[0]+'__'+name[1])
#print(transfer2,value1,value2)
        if transfer2 not in folder_naming:
            file_transfer=open(transfer2+".txt",'w')
            file_transfer.write(total)
            file_transfer.close()
            #print(transfer1)
    print(datetime.datetime.now())

    new_folder_4transfer=os.listdir(path_folder)
    for file_transferingddd in new_folder_4transfer:
        pause_time=-math.log(random.uniform(0, 1))
        file_transferingdd=file_transferingddd.split('.')
        file_transferingd=file_transferingdd[0].split('_')
        if len(file_transferingddd) > 17:
            if file_transferingd[0]==jeffdean1[0] or file_transferingd[1] ==jeffdean1[0]:
                if file_transferingd[5]==jeffdean1[0] or file_transferingd[6] ==jeffdean1[0]:
                    seven="coded_"+file_transferingd[3]
                    fifteen="coded_"+file_transferingd[8]
                    #print(file_transferingddd ,seven,fifteen)
                        #print(file_transferingd)
                    if not os.path.exists("/Users/xiaoran/dropbox/cache_map/"+seven+'/'+file_transferingddd):
                        shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_'+jeffdean1[0]+'/'+file_transferingddd,'/Users/xiaoran/dropbox/cache_map/'+seven)
                    if not os.path.exists("/Users/xiaoran/dropbox/cache_map/"+fifteen+'/'+file_transferingddd):
                        shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_'+jeffdean1[0]+'/'+file_transferingddd, '/Users/xiaoran/dropbox/cache_map/'+fifteen)
                    time.sleep(0.1)
#print("send hellowold"+file_transferingddd)

############### Part 5  ##################
############ Decoding Code ###############
def Decoding(val1):
    jeffdean1=val1
    foldervalue=jeffdean1[0]
    jeffdeanlist=jeffdean1[1]
    path_folder="/Users/xiaoran/dropbox/cache_map/coded_"+jeffdean1[0]
    os.chdir(path_folder)
    print("current Decoding user" + jeffdean1[0])
    for index, i in enumerate(jeffdeanlist):
        value1=i[1]
        value2=i[2]
        if value1 > value2:
            if jeffdean1[0]>value1 and jeffdean1[0]>value2:
            #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                file1=value1+"_"+jeffdean1[0]+"_1_"+value2
                f1=open(path_folder+"/"+file1+".txt",'r')
                a=int(f1.read())
                f1.close()
                #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                file2=value2+"_"+jeffdean1[0]+"_1_"+value1
                f2=open(path_folder+"/"+file2+".txt",'r')
                b=int(f2.read())
                f2.close()
                file3=value2+"_"+value1+"_2_"+jeffdean1[0]+"__"+file1
                f3=open(path_folder+"/"+file3+".txt",'r')
                c=int(f3.read())
                f3.close()
                file4=value2+"_"+value1+"_1_"+jeffdean1[0]+"__"+file2
                f4=open(path_folder+"/"+file4+".txt",'r')
                d=int(f4.read())
                f4.close()
                substrate=str(c-a)
                substrates=str(d-b)
                decodefile1=value2+"_"+value1+"_2_"+jeffdean1[0]
                decodefile2=value2+"_"+value1+"_1_"+jeffdean1[0]
                file_decode=open(decodefile1+".txt",'w')
                file_decode.write(substrate)
                file_decode.close()
                file_decodes=open(decodefile2+".txt",'w')
                file_decodes.write(substrates)
                file_decodes.close()
            elif jeffdean1[0]>value2 and jeffdean1[0]<value1:
                #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                file1=jeffdean1[0]+"_"+value1+"_2_"+value2
                f1=open(path_folder+"/"+file1+".txt",'r')
                a=int(f1.read())
                f1.close()
                #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                file2=value2+"_"+jeffdean1[0]+"_1_"+value1
                f2=open(path_folder+"/"+file2+".txt",'r')
                b=int(f2.read())
                f2.close()
                file3=value2+"_"+value1+"_2_"+jeffdean1[0]+"__"+file1
                f3=open(path_folder+"/"+file3+".txt",'r')
                c=int(f3.read())
                f3.close()
                file4=file2+"__"+value2+"_"+value1+"_1_"+jeffdean1[0]
                f4=open(path_folder+"/"+file4+".txt",'r')
                d=int(f4.read())
                f4.close()
                substrate=str(c-a)
                substrates=str(d-b)
                decodefile1=value2+"_"+value1+"_2_"+jeffdean1[0]
                decodefile2=value2+"_"+value1+"_1_"+jeffdean1[0]
                file_decode=open(decodefile1+".txt",'w')
                file_decode.write(substrate)
                file_decode.close()
                file_decodes=open(decodefile2+".txt",'w')
                file_decodes.write(substrates)
                file_decodes.close()
            elif jeffdean1[0]<value1 and jeffdean1[0]<value2:
            #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                file1=jeffdean1[0]+"_"+value1+"_2_"+value2
                f1=open(path_folder+"/"+file1+".txt",'r')
                a=int(f1.read())
                f1.close()
                #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                file2=jeffdean1[0]+"_"+value2+"_2_"+value1
                f2=open(path_folder+"/"+file2+".txt",'r')
                b=int(f2.read())
                f2.close()
                file3=file1+"__"+value2+"_"+value1+"_2_"+jeffdean1[0]
                f3=open(path_folder+"/"+file3+".txt",'r')
                c=int(f3.read())
                f3.close()
                file4=file2+"__"+value2+"_"+value1+"_1_"+jeffdean1[0]
                f4=open(path_folder+"/"+file4+".txt",'r')
                d=int(f4.read())
                f4.close()
                substrate=str(c-a)
                substrates=str(d-b)
                decodefile1=value2+"_"+value1+"_2_"+jeffdean1[0]
                decodefile2=value2+"_"+value1+"_1_"+jeffdean1[0]
                file_decode=open(decodefile1+".txt",'w')
                file_decode.write(substrate)
                file_decode.close()
                file_decodes=open(decodefile2+".txt",'w')
                file_decodes.write(substrates)
                file_decodes.close()
        else:
            if jeffdean1[0]>value1 and jeffdean1[0]>value2:
                #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                file1=value1+"_"+jeffdean1[0]+"_1_"+value2
                f1=open(path_folder+"/"+file1+".txt",'r')
                a=int(f1.read())
                f1.close()
                #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                file2=value2+"_"+jeffdean1[0]+"_1_"+value1
                f2=open(path_folder+"/"+file2+".txt",'r')
                b=int(f2.read())
                f2.close()
                file3=value1+"_"+value2+"_1_"+jeffdean1[0]+"__"+file1
                f3=open(path_folder+"/"+file3+".txt",'r')
                c=int(f3.read())
                f3.close()
                file4=value1+"_"+value2+"_2_"+jeffdean1[0]+"__"+file2
                f4=open(path_folder+"/"+file4+".txt",'r')
                d=int(f4.read())
                f4.close()
                substrate=str(c-a)
                substrates=str(d-b)
                decodefile1=value1+"_"+value2+"_1_"+jeffdean1[0]
                decodefile2=value1+"_"+value2+"_2_"+jeffdean1[0]
                file_decode=open(decodefile1+".txt",'w')
                file_decode.write(substrate)
                file_decode.close()
                file_decodes=open(decodefile2+".txt",'w')
                file_decodes.write(substrates)
                file_decodes.close()
            elif jeffdean1[0]>value1 and jeffdean1[0]<value2:
                #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                file1=value1+"_"+jeffdean1[0]+"_1_"+value2
                f1=open(path_folder+"/"+file1+".txt",'r')
                a=int(f1.read())
                f1.close()
                #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                file2=jeffdean1[0]+"_"+value2+"_2_"+value1
                f2=open(path_folder+"/"+file2+".txt",'r')
                b=int(f2.read())
                f2.close()
                file3=file1+"__"+value1+"_"+value2+"_1_"+jeffdean1[0]
                f3=open(path_folder+"/"+file3+".txt",'r')
                c=int(f3.read())
                f3.close()
                file4=value1+"_"+value2+"_2_"+jeffdean1[0]+"__"+file2
                f4=open(path_folder+"/"+file4+".txt",'r')
                d=int(f4.read())
                f4.close()
                substrate=str(c-a)
                substrates=str(d-b)
                decodefile1=value1+"_"+value2+"_1_"+jeffdean1[0]
                decodefile2=value1+"_"+value2+"_2_"+jeffdean1[0]
                file_decode=open(decodefile1+".txt",'w')
                file_decode.write(substrate)
                file_decode.close()
                file_decodes=open(decodefile2+".txt",'w')
                file_decodes.write(substrates)
                file_decodes.close()
            elif jeffdean1[0]<value1 and jeffdean1[0]<value2:
                #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                file1=jeffdean1[0]+"_"+value1+"_2_"+value2
                f1=open(path_folder+"/"+file1+".txt",'r')
                a=int(f1.read())
                f1.close()
                #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                file2=jeffdean1[0]+"_"+value2+"_2_"+value1
                f2=open(path_folder+"/"+file2+".txt",'r')
                b=int(f2.read())
                f2.close()
                file3=file1+"__"+value1+"_"+value2+"_1_"+jeffdean1[0]
                f3=open(path_folder+"/"+file3+".txt",'r')
                c=int(f3.read())
                f3.close()
                file4=file2+"__"+value1+"_"+value2+"_2_"+jeffdean1[0]
                f4=open(path_folder+"/"+file4+".txt",'r')
                d=int(f4.read())
                f4.close()
                substrate=str(c-a)
                substrates=str(d-b)
                decodefile1=value1+"_"+value2+"_1_"+jeffdean1[0]
                decodefile2=value1+"_"+value2+"_2_"+jeffdean1[0]
                file_decode=open(decodefile1+".txt",'w')
                file_decode.write(substrate)
                file_decode.close()
                file_decodes=open(decodefile2+".txt",'w')
                file_decodes.write(substrates)
                file_decodes.close()


if __name__ == "__main__":
    path ="/Users/xiaoran/dropbox/cache_map"
    folder_path="/Users/xiaoran/dropbox/cache_map/coded_master"
    def moveFileto(sourceDir,  targetDir):
        shutil.copy(sourceDir,  targetDir)

    if os.path.exists(folder_path): #Delete the folder if the folder exist
        shutil.rmtree(folder_path)
    print("How many user you are trying to have?")
    user=input()
    users=int(user)
    counter=int(user)
    userss=str(user)
    print("you are going to have " +user + " users for this simulation" )

    #filecreating()#creating files and folder

    #def filecreating():
    files= os.listdir(path) #get file name under the folder
    # define the access rights
    access_rights = 0o755

    try:
        os.mkdir(folder_path, access_rights)
    except OSError:
        print ("Creation of the directory %s failed" % folder_path)
    os.chdir(folder_path)#change the director for the folder path
    filecreator()
    user_name, temp2 = Mapping()
    everything=shufgen(temp2)
    print("Helloworld")
    print( everything)
    pool=multiprocessing.Pool(processes = users)
    pool2=multiprocessing.Pool(processes = users)
    start1 =datetime.datetime.now()
    for i in everything:
        print("Server current encoding coded" + i[0])
        jeffdean=i[0]
        print(datetime.datetime.now())
        pool.apply_async(Encoding, [i])
        print("Done")
    pool.close()
    pool.join()
    print("finished all the shuffling, Now start the decoding")
    start2 =datetime.datetime.now()

    for i in everything:
        print("Server current decoding coded" + i[0])
        jeffdean=i[0]
        print(datetime.datetime.now())
        pool2.apply_async(Decoding, [i])
        print("Done")
    pool2.close()
    pool2.join()
    finish=datetime.datetime.now()
    print("For " + userss +" users spent \{}".format(finish-start1))
    print("For " + userss +" users encoding spent \{}".format(start2-start1))



