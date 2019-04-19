import os
import shutil
import math
import random
import multiprocessing
import time
class FileTransfer(object):
    def __init__(self, users, folder_path,path):
        #self.file_dir = file_dir
        self.users = users
        self.folder_path=folder_path
        self.path=path

################ Part 1  #################
############# Mapping Code  ##############
    def Mapping(self):
        new_path=self.folder_path+"pair_dir/bin_dir/"
        files= os.listdir(new_path) #get file name under the folder
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
        os.chdir(self.path)#change the director for the folder path
        #print(results)
        for folder_name in results:#delete folders that exists from previous run
            if os.path.exists(self.path+ folder_name):
                shutil.rmtree(self.path+ folder_name)
        for folder_name in results:#create new folders for the number desired
            if os.path.isdir(self.path):
                os.mkdir(os.path.join(self.path, folder_name))
        counter=0
        for files_names in files:
            files_name=files_names.split('.')
            file_name=files_name[0].split('_')
            if len(files_names) > 4:
                first="coded_"+file_name[0]
                third="coded_"+file_name[1]
                shutil.copy(new_path+files_names, self.path+first)
                shutil.copy(new_path+files_names, self.path+third)
        return results,number_result
#['coded_1', 'coded_3', 'coded_2', 'coded_4'] ['3', '1', '4', '2']


################ Part 3  #################
############ Call Function  ##############  naive
    def Call_naive_function(self, everything):
        pool=multiprocessing.Pool(processes = int(self.users))
        for i in everything:
            jeffdean=i[0]
            pool.apply_async(self.Naive_Encoding, [i])
#            print("Server current running " + i)
#            pool.apply_async(self.Naive_Encoding, (i,))
        pool.close()
        pool.join()
        print("Done")


################ Part 4  #################
############# Naive Code  ################
    def Naive_Encoding(self,everything):
        counter=0
        jeffdean1=everything
        foldervalue=jeffdean1[0]
        jeffdeanlist=jeffdean1[1]
        #for thread_name in results:
        thread_path=self.path+"coded_"+jeffdean1[0]
        os.chdir(thread_path)
        folder_naming=[]
        for index, i in enumerate(jeffdeanlist):
            value1=i[1]
            value2=i[2]
            gau_pause_time=-math.log(random.uniform(0, 1))#gaussian distribution
            file_trans_location='/Users/xiaoran/dropbox/cache_map/coded_'+value2
            if jeffdean1[0] >value1:
                file_named_1=value1+"_"+jeffdean1[0]+"_1_"+value2+".txt"
                file_named_2=value1+"_"+jeffdean1[0]+"_2_"+value2+".txt"
                counter+=2
                time.sleep(0.2)
                shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_'+jeffdean1[0]+'/'+file_named_2,file_trans_location)
                shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_'+value1+'/'+file_named_1,file_trans_location)
            else:
                file_named_1=jeffdean1[0]+"_"+value1+"_1_"+value2+".txt"
                file_named_2=jeffdean1[0]+"_"+value1+"_2_"+value2+".txt"
                counter+=2
                time.sleep(0.2)
                shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_'+jeffdean1[0]+'/'+file_named_1,file_trans_location)
                shutil.copy('/Users/xiaoran/dropbox/cache_map/coded_'+value1+'/'+file_named_2,file_trans_location)

'''
        print("Helloworld"+thread_path)
        for file_copy in location:
            gau_pause_time=-math.log(random.uniform(0, 1))#gaussian distribution
            result_file_copy=file_copy.split('_')
            if len(result_file_copy) >3:
                print(file_copy)
                first=result_file_copy[0]
                third=result_file_copy[1]
                fifth=result_file_copy[2]
                seventh=result_file_copy[3]
                file_location=self.path+'coded_'+seventh
                #print(first, third, fifth, seventh)
                if (seventh != first and seventh!=third and (fifth =="1")): # if equal to 1 then copy file from location equal to the value from first
                    shutil.copy(self.path+'coded_'+first+'/'+file_copy, file_location)
                elif (seventh != first and seventh!=third and (fifth =="2")): # if equal to 2 then copy file from location equal to the value from second
                    shutil.copy(self.path+ 'coded_'+third+'/'+file_copy, file_location)
'''
