import os
import shutil
import multiprocessing
import math
import random
import time,datetime
import multiprocessing
from BinaryTool import BinaryTool
import threading

class FileCodedTransfer(object):
    def __init__(self, users, folder_path,path):
        #self.file_dir = file_dir
        self.users = users
        self.folder_path=folder_path
        self.path=path


################ Part 3  #################
############ Call Function  ##############  coded
    def Call_coded_function(self, everything):
        #L5=everything
        pool=multiprocessing.Pool(processes = int(self.users))
        pool2=multiprocessing.Pool(processes = int(self.users))
        start1 = datetime.datetime.now()
        threads_encode = []

        #Create a single thread for each worker
        for i in everything:
            print("Server current encoding coded" + str(i[0]))
            jeffdean = i[0]
            print(datetime.datetime.now())
            t = threading.Thread(target=self.coded_Encoding, args=(i,))
            threads_encode.append(t)
            t.start()

        #Wait until all workers are done with their job
        for x in threads_encode:
            x.join()

        threads_decode = []
        print("All workers done encoding")
        print("finished all the shuffling, Now start the decoding")
        start2 = datetime.datetime.now()

        for i in everything:
            print("Server current decoding coded" + str(i[0]))
            print(datetime.datetime.now())
            t = threading.Thread(target=self.Decoding, args=(i,))
            threads_decode.append(t)
            t.start()
        # Wait until all workers are done with their job
        for x in threads_decode:
            x.join()

        # pool2.close()
        # pool2.join()
        finish=datetime.datetime.now()
        print("For " + self.users +" users spent \{}".format(finish-start1))
        print("For " + self.users +" users encoding spent \{}".format(start2-start1))

################ Part 5  #################
############# Coded Code  ################

############### Part 51 ##################
##### Shuffling Code for generate ########
    def shufgen(self):
        L1=[]
        user=int(self.users)
        for i in range(user):
            i=i+1
            L1.append(i)
        #L1=number_result
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


############### Part 52  ##################
############ Shuffling Code ##############
#print (results)
    def coded_Encoding(self,i):
        jeffdean1=i
        worker_id = jeffdean1[0]
        jeffdeanlist=jeffdean1[1]

        print(jeffdeanlist)
        #for new_folder_name in results:#create new file in different folder
        path_folder=self.path+"coded_" + str(jeffdean1[0])
        os.chdir(path_folder)
        bi_tool = BinaryTool(path_folder)

        for index, i in enumerate(jeffdeanlist):
            beta = i[1]#value 1
            theta = i[2]#value 2
            beta_str = str(beta)
            theta_str = str(theta)
            sub_name_list = []
            worker_id_str = str(worker_id)#jeffdean1[0]
            if beta > worker_id:
                file1=worker_id_str+"_"+beta_str+"_1_"+theta_str
                with open(self.path+"coded_"+str(jeffdean1[0])+"/"+worker_id_str+"_"+beta_str+"_1_"+theta_str+".txt",'r') as f1:
                    sub_name_list.append(file1)
                    bin_a = f1.read()
            else:
                file1=beta_str+"_"+worker_id_str+"_2_"+ theta_str
                with open(self.path+"coded_"+str(jeffdean1[0])+"/"+beta_str+"_"+worker_id_str+"_2_"+theta_str+".txt",'r') as f1:
                    sub_name_list.append(file1)
                    bin_a = f1.read()
            if theta > worker_id:
                file2=worker_id_str+"_"+ theta_str +"_1_"+beta_str
                with open(self.path+"coded_"+str(jeffdean1[0])+"/"+worker_id_str+"_"+theta_str+"_1_"+beta_str+".txt",'r') as f2:
                    sub_name_list.append(file2)
                    bin_b = f2.read()
            else:
                file2=theta_str + "_" + worker_id_str + "_2_"+ beta_str
                with open(self.path+"coded_"+str(jeffdean1[0])+"/"+theta_str+"_"+worker_id_str+"_2_"+beta_str+".txt",'r') as f2:
                    sub_name_list.append(file2)
                    bin_b = f2.read()
            total= bi_tool.Xor(bin_a, bin_b)

            #The xor output file of file A and file B is named as fileA__fileB
            if beta >theta:
                transfer2=str(sub_name_list[1]+'__'+sub_name_list[0])
            else:
                transfer2=str(sub_name_list[0]+'__'+sub_name_list[1])

            xor_dir = path_folder + '/'
            if not os.path.isdir(xor_dir):
                os.mkdir(xor_dir)

            if transfer2 not in sub_name_list:
                print("Write files:", transfer2 + ".txt")
                file_transfer=open(xor_dir + transfer2+".txt",'w')
                file_transfer.write(total)
                file_transfer.close()

        src_dir = path_folder + '/'

        #worker_num_str is the string format of current worker number
        worker_num_str = str(jeffdean1[0])

        #After the encoding is done, all the xor files should be inside of the "/xored_files/" of each workers, the the each worker starts sending files
        print(str(jeffdean1[0]) + " starts sending files")
        for src_file in os.listdir(src_dir):
            pause_time=-math.log(random.uniform(0, 1))
            file_name = src_file.split('.')
            file_name_list=file_name[0].split('_')
            if len(src_file) > 17:
                #Compare if the alpha or beta of the file A is equal to the current worker number
                if file_name_list[0]== worker_num_str or file_name_list[1] == worker_num_str:
                    # Compare if the alpha or beta of the file B is equal to the current worker number
                    if file_name_list[5] == worker_num_str or file_name_list[6] == worker_num_str:

                        #Creating destination for the file to be sent based on the value of last digit of file A and file B
                        dest_1 = self.path + "coded_"+file_name_list[3] + '/'
                        dest_2 = self.path + "coded_"+file_name_list[8] + '/'
                        # print(str(jeffdean1[0]), "dest1: " + dest_1, "dest2:" + dest_2)
                        if not os.path.isdir(dest_1):
                            print("Creating", dest_1)
                            os.mkdir(dest_1)
                        if not os.path.isdir(dest_2):
                            os.mkdir(dest_2)
                            print("Creating", dest_2)

                        #Here we use file copy to implement the file sending
                        if not os.path.exists(dest_1 + src_file):
                            shutil.copy(src_dir + src_file, dest_1)
                        if not os.path.exists(dest_2  + src_file):
                            shutil.copy(src_dir + src_file, dest_2)
                        time.sleep(0.1)

    def Decoding(self, val1):
        jeffdean1=val1
        foldervalue=str(jeffdean1[0])
        jeffdeanlist=jeffdean1[1]
        path_folder=self.path + "coded_" + str(jeffdean1[0])
        os.chdir(path_folder)
        jeffdean1[0] = str(jeffdean1[0])

        print("current Decoding user" + jeffdean1[0])
        binary_tool = BinaryTool("")

        def write_file(filename, content):
            with open(filename + ".txt", 'w') as f:
                f.write(content)

        for index, i in enumerate(jeffdeanlist):
            value1=str(i[1])
            value2=str(i[2])
            if value1 > value2:
                if jeffdean1[0]>value1 and jeffdean1[0]>value2:
                #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                    file1=value1+"_"+jeffdean1[0]+"_1_"+value2
                    f1=open(path_folder+"/"+file1+".txt",'r')
                    # a=int(f1.read())
                    f1.close()
                    #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                    file2=value2+"_"+jeffdean1[0]+"_1_"+value1
                    f2=open(path_folder+"/"+file2+".txt",'r')
                    # b=int(f2.read())
                    f2.close()
                    file3=value2+"_"+value1+"_2_"+jeffdean1[0]+"__"+file1
                    f3=open(path_folder+"/"+file3+".txt",'r')
                    # c=int(f3.read())
                    f3.close()
                    file4=value2+"_"+value1+"_1_"+jeffdean1[0]+"__"+file2
                    f4=open(path_folder+"/"+file4+".txt",'r')
                    # d=int(f4.read())
                    f4.close()
                    file1 = path_folder+"/"+ file1 + ".txt"
                    file2 = path_folder+"/"+ file2 + ".txt"
                    file3 = path_folder+"/"+ file3 + ".txt"
                    file4 = path_folder+"/"+ file4 + ".txt"
                    substrate=binary_tool.xorTowFiles(file3, file1)
                    substrates=binary_tool.xorTowFiles(file4, file2)
                    # print("fuck world:",substrate, substrates)
                    decodefile1=value2+"_"+value1+"_2_"+jeffdean1[0]
                    decodefile2=value2+"_"+value1+"_1_"+jeffdean1[0]

                    write_file(path_folder + "/" + decodefile1, substrate)
                    write_file(path_folder + "/" + decodefile2, substrates)

                    # file_decode=open(decodefile1+".txt",'w')
                    # file_decode.write(substrate)
                    # file_decode.close()
                    # file_decodes=open(decodefile2+".txt",'w')
                    # file_decodes.write(substrates)
                    # file_decodes.close()
                elif jeffdean1[0]>value2 and jeffdean1[0]<value1:
                    #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                    file1=jeffdean1[0]+"_"+value1+"_2_"+value2
                    f1=open(path_folder+"/"+file1+".txt",'r')
                    # a=int(f1.read())
                    f1.close()
                    #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                    file2=value2+"_"+jeffdean1[0]+"_1_"+value1
                    f2=open(path_folder+"/"+file2+".txt",'r')
                    # b=int(f2.read())
                    f2.close()
                    file3=value2+"_"+value1+"_2_"+jeffdean1[0]+"__"+file1
                    f3=open(path_folder+"/"+file3+".txt",'r')
                    # c=int(f3.read())
                    f3.close()
                    file4=file2+"__"+value2+"_"+value1+"_1_"+jeffdean1[0]
                    f4=open(path_folder+"/"+file4+".txt",'r')
                    # d=int(f4.read())
                    f4.close()
                    # substrate=str(c-a)
                    # substrates=str(d-b)
                    file1 = path_folder+"/"+ file1 + ".txt"
                    file2 = path_folder+"/"+ file2 + ".txt"
                    file3 = path_folder+"/"+ file3 + ".txt"
                    file4 = path_folder+"/"+ file4 + ".txt"
                    substrate = binary_tool.xorTowFiles(file3, file1)
                    substrates = binary_tool.xorTowFiles(file4, file2)
                    decodefile1=value2+"_"+value1+"_2_"+jeffdean1[0]
                    decodefile2=value2+"_"+value1+"_1_"+jeffdean1[0]

                    # print("fuck: ", jeffdean1[0], decodefile1, decodefile2)
                    write_file(path_folder+"/" + decodefile1, substrate)
                    write_file(path_folder+"/" + decodefile2, substrates)

                    # file_decode=open(decodefile1+".txt",'w')
                    # file_decode.write(substrate)
                    # file_decode.close()
                    # file_decodes=open(decodefile2+".txt",'w')
                    # file_decodes.write(substrates)
                    # file_decodes.close()
                elif jeffdean1[0]<value1 and jeffdean1[0]<value2:
                #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                    file1=jeffdean1[0]+"_"+value1+"_2_"+value2
                    f1=open(path_folder+"/"+file1+".txt",'r')
                    # a=int(f1.read())
                    f1.close()
                    #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                    file2=jeffdean1[0]+"_"+value2+"_2_"+value1
                    f2=open(path_folder+"/"+file2+".txt",'r')
                    # b=int(f2.read())
                    f2.close()
                    file3=file1+"__"+value2+"_"+value1+"_2_"+jeffdean1[0]
                    f3=open(path_folder+"/"+file3+".txt",'r')
                    # c=int(f3.read())
                    f3.close()
                    file4=file2+"__"+value2+"_"+value1+"_1_"+jeffdean1[0]
                    f4=open(path_folder+"/"+file4+".txt",'r')
                    # d=int(f4.read())
                    f4.close()
                    # substrate=str(c-a)
                    # substrates=str(d-b)
                    file1 = path_folder+"/"+ file1 + ".txt"
                    file2 = path_folder+"/"+ file2 + ".txt"
                    file3 = path_folder+"/"+ file3 + ".txt"
                    file4 = path_folder+"/"+ file4 + ".txt"
                    substrate = binary_tool.xorTowFiles(file3, file1)
                    substrates = binary_tool.xorTowFiles(file4, file2)
                    decodefile1=value2+"_"+value1+"_2_"+jeffdean1[0]
                    decodefile2=value2+"_"+value1+"_1_"+jeffdean1[0]
                    write_file(path_folder + "/" + decodefile1, substrate)
                    write_file(path_folder + "/" + decodefile2, substrates)
                # file_decode=open(decodefile1+".txt",'w')
                    # file_decode.write(substrate)
                    # file_decode.close()
                    # file_decodes=open(decodefile2+".txt",'w')
                    # file_decodes.write(substrates)
                    # file_decodes.close()
            else:
                if jeffdean1[0]>value1 and jeffdean1[0]>value2:
                    #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                    file1=value1+"_"+jeffdean1[0]+"_1_"+value2
                    f1=open(path_folder+"/"+file1+".txt",'r')
                    # a=int(f1.read())
                    f1.close()
                    #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                    file2=value2+"_"+jeffdean1[0]+"_1_"+value1
                    f2=open(path_folder+"/"+file2+".txt",'r')
                    # b=int(f2.read())
                    f2.close()
                    file3=value1+"_"+value2+"_1_"+jeffdean1[0]+"__"+file1
                    f3=open(path_folder+"/"+file3+".txt",'r')
                    # c=int(f3.read())
                    f3.close()
                    file4=value1+"_"+value2+"_2_"+jeffdean1[0]+"__"+file2
                    f4=open(path_folder+"/"+file4+".txt",'r')
                    # d=int(f4.read())
                    f4.close()
                    # substrate=str(c-a)
                    # substrates=str(d-b)
                    file1 = path_folder+"/"+ file1 + ".txt"
                    file2 = path_folder+"/"+ file2 + ".txt"
                    file3 = path_folder+"/"+ file3 + ".txt"
                    file4 = path_folder+"/"+ file4 + ".txt"
                    substrate = binary_tool.xorTowFiles(file3, file1)
                    substrates = binary_tool.xorTowFiles(file4, file2)
                    decodefile1=value1+"_"+value2+"_1_"+jeffdean1[0]
                    decodefile2=value1+"_"+value2+"_2_"+jeffdean1[0]
                    write_file(path_folder + "/" + decodefile1, substrate)
                    write_file(path_folder + "/" + decodefile2, substrates)
                    # file_decode=open(decodefile1+".txt",'w')
                    # file_decode.write(substrate)
                    # file_decode.close()
                    # file_decodes=open(decodefile2+".txt",'w')
                    # file_decodes.write(substrates)
                    # file_decodes.close()
                elif jeffdean1[0]>value1 and jeffdean1[0]<value2:
                    #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                    file1=value1+"_"+jeffdean1[0]+"_1_"+value2
                    f1=open(path_folder+"/"+file1+".txt",'r')
                    # a=int(f1.read())
                    f1.close()
                    #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                    file2=jeffdean1[0]+"_"+value2+"_2_"+value1
                    f2=open(path_folder+"/"+file2+".txt",'r')
                    # b=int(f2.read())
                    f2.close()
                    file3=file1+"__"+value1+"_"+value2+"_1_"+jeffdean1[0]
                    f3=open(path_folder+"/"+file3+".txt",'r')
                    # c=int(f3.read())
                    f3.close()
                    file4=value1+"_"+value2+"_2_"+jeffdean1[0]+"__"+file2
                    f4=open(path_folder+"/"+file4+".txt",'r')
                    # d=int(f4.read())
                    f4.close()
                    # substrate=str(c-a)
                    # substrates=str(d-b)
                    file1 = path_folder+"/"+ file1 + ".txt"
                    file2 = path_folder+"/"+ file2 + ".txt"
                    file3 = path_folder+"/"+ file3 + ".txt"
                    file4 = path_folder+"/"+ file4 + ".txt"
                    substrate = binary_tool.xorTowFiles(file3, file1)
                    substrates = binary_tool.xorTowFiles(file4, file2)
                    decodefile1=value1+"_"+value2+"_1_"+jeffdean1[0]
                    decodefile2=value1+"_"+value2+"_2_"+jeffdean1[0]
                    write_file(path_folder + "/" + decodefile1, substrate)
                    write_file(path_folder + "/" + decodefile2, substrates)

                    # file_decode=open(decodefile1+".txt",'w')
                    # file_decode.write(substrate)
                    # file_decode.close()
                    # file_decodes=open(decodefile2+".txt",'w')
                    # file_decodes.write(substrates)
                    # file_decodes.close()
                elif jeffdean1[0]<value1 and jeffdean1[0]<value2:
                    #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
                    file1=jeffdean1[0]+"_"+value1+"_2_"+value2
                    f1=open(path_folder+"/"+file1+".txt",'r')
                    # a=int(f1.read())
                    f1.close()
                    #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
                    file2=jeffdean1[0]+"_"+value2+"_2_"+value1
                    f2=open(path_folder+"/"+file2+".txt",'r')
                    # b=int(f2.read())
                    f2.close()
                    file3=file1+"__"+value1+"_"+value2+"_1_"+jeffdean1[0]
                    f3=open(path_folder+"/"+file3+".txt",'r')
                    # c=int(f3.read())
                    f3.close()
                    file4=file2+"__"+value1+"_"+value2+"_2_"+jeffdean1[0]
                    f4=open(path_folder+"/"+file4+".txt",'r')
                    # d=int(f4.read())
                    f4.close()
                    file1 = path_folder+"/"+ file1 + ".txt"
                    file2 = path_folder+"/"+ file2 + ".txt"
                    file3 = path_folder+"/"+ file3 + ".txt"
                    file4 = path_folder+"/"+ file4 + ".txt"
                    # substrate=str(c-a)
                    # substrates=str(d-b)
                    substrate = binary_tool.xorTowFiles(file3, file1)
                    substrates = binary_tool.xorTowFiles(file4, file2)
                    decodefile1=value1+"_"+value2+"_1_"+jeffdean1[0]
                    decodefile2=value1+"_"+value2+"_2_"+jeffdean1[0]
                    write_file(path_folder + "/" + decodefile1, substrate)
                    write_file(path_folder + "/" + decodefile2, substrates)

                    # file_decode=open(decodefile1+".txt",'w')
                    # file_decode.write(substrate)
                    # file_decode.close()
                    # file_decodes=open(decodefile2+".txt",'w')
                    # file_decodes.write(substrates)
                    # file_decodes.close()




############### Part 53  ##################
############ Decoding Code ###############
#     def Decoding(self, val1):
#         binary_tool = BinaryTool("")
#
#         def xor_and_write(f1, f2, f3, f4, str_val1, str_val2):
#             xor_ca = binary_tool.xorTowFiles(f1, f3, False)
#             xor_db = binary_tool.xorTowFiles(f2, f4, False)
#             decodefile1 = str_val2 + "_" + str_val1 + "_2_" + str(jeffdean1[0])
#             decodefile2 =  str_val2 + "_" + str_val1 + "_1_" + str(jeffdean1[0])
#             with open(path_folder + "/"  + decodefile1+".txt",'w') as f:
#                 f.write(xor_ca)
#             with open(path_folder + "/" + decodefile2+".txt",'w') as f:
#                 f.write(xor_db)
#
#         print("Decode parameter:",val1)
#         jeffdean1=val1
#         foldervalue=jeffdean1[0]
#         jeffdeanlist=jeffdean1[1]
#         path_folder= self.path+"coded_"+ str(foldervalue)
#         os.chdir(path_folder)
#         print("current Decoding user", jeffdean1[0])
#         for index, i in enumerate(jeffdeanlist):
#             value1=i[1]
#             value2=i[2]
#             str_value1 = str(value1)
#             str_value2 = str(value2)
#             if value1 > value2:
#                 if jeffdean1[0]>value1 and jeffdean1[0]>value2:
#                     #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
#                     file1 = str_value1+"_"+str(foldervalue)+"_1_"+str_value2
#                     #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
#                     file2 = str_value2 + "_"+str(foldervalue)+"_1_"+str_value1
#                     file3 = str_value2+"_"+str_value1+"_2_"+str(foldervalue)+"__"+file1
#                     file4 = str_value2+"_"+str_value1+"_1_"+str(foldervalue)+"__"+file2
#
#                     file1 = path_folder + "/" + file1 + ".txt"
#                     file2 = path_folder + "/" + file2 + ".txt"
#                     file3 = path_folder + "/" + file3 + ".txt"
#                     file4 = path_folder + "/" + file4 + ".txt"
#                     xor_and_write(file1, file2, file3, file4, str_value1, str_value2)
#
#                 elif jeffdean1[0]>value2 and jeffdean1[0]<value1:
#                     #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
#                     file1 = str(foldervalue)+"_"+str_value1+"_2_"+str_value2
#                     #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
#                     file2 = str_value2 + "_" + str(foldervalue) + "_1_" + str_value1
#                     file3 = str_value2 + "_" + str_value1+"_2_" + str(foldervalue) + "__" + file1
#                     file4 = file2+"__"+str_value2+"_"+str_value1+"_1_"+str(foldervalue)
#
#                     file1 = path_folder + "/" + file1 + ".txt"
#                     file2 = path_folder + "/" + file2 + ".txt"
#                     file3 = path_folder + "/" + file3 + ".txt"
#                     file4 = path_folder + "/" + file4 + ".txt"
#
#                     xor_and_write(file1, file2, file3, file4, str_value1, str_value2)
#
#                 elif jeffdean1[0]<value1 and jeffdean1[0]<value2:
#                     #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
#                     file1=str(foldervalue)+"_"+ str_value1 +"_2_"+str_value2
#                     #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
#                     file2=str(foldervalue)+"_"+str_value2+"_2_"+str_value1
#                     file3=file1+"__"+str_value2+"_"+str_value1+"_2_"+str(foldervalue)
#                     file4=file2+"__"+str_value2+"_"+str_value1+"_1_"+str(foldervalue)
#
#                     file1 = path_folder + "/" + file1 + ".txt"
#                     file2 = path_folder + "/" + file2 + ".txt"
#                     file3 = path_folder + "/" + file3 + ".txt"
#                     file4 = path_folder + "/" + file4 + ".txt"
#
#                     xor_and_write(file1, file2, file3, file4, str_value1, str_value2)
#
#         else:
#             if jeffdean1[0]>value1 and jeffdean1[0]>value2:
#
#                 file1 = str_value1 + "_" + str(foldervalue) + "_1_" + str_value2
#                 # if coming from value2 The value exist in the file is  V1_num[1]_1_v2
#                 file2 = str_value2 + "_" + str(foldervalue) + "_1_" + str_value1
#                 file3 = str_value2 + "_" + str_value1 + "_1_" + str(foldervalue) + "__" + file1
#                 file4 = str_value2 + "_" + str_value1 + "_2_" + str(foldervalue) + "__" + file2
#
#                 file1 = path_folder + "/" + file1 + ".txt"
#                 file2 = path_folder + "/" + file2 + ".txt"
#                 file3 = path_folder + "/" + file3 + ".txt"
#                 file4 = path_folder + "/" + file4 + ".txt"
#
#                 print("files to be processed:",file1, file2, file3, file4)
#                 xor_and_write(file1, file2, file3, file4, str_value1, str_value2)
# '''
#             elif jeffdean1[0]>value1 and jeffdean1[0]<value2:
#                 #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
#                 file1 = str_value1 + "_"+str(jeffdean1[0])+"_1_"+str_value2
#                 #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
#                 file2 = str(jeffdean1[0])+"_"+str_value2+"_2_"+str_value1
#
#                 file3 = file1+"__"+str_value1+"_"+str_value2+"_1_"+str(jeffdean1[0])
#                 file4 = str_value1+"_"+str_value2+"_2_"+str(jeffdean1[0])+"__"+file2
#
#                 file1 = path_folder + "/" + file1 + ".txt"
#                 file2 = path_folder + "/" + file2 + ".txt"
#                 file3 = path_folder + "/" + file3 + ".txt"
#                 file4 = path_folder + "/" + file4 + ".txt"
#
#                 xor_and_write(file1, file2, file3, file4, str_value1, str_value2)
#
#             elif jeffdean1[0]<value1 and jeffdean1[0]<value2:
#                 #if coming from value1. The value exist in the file is  V1_num[1]_1_v2
#                 file1 = str(jeffdean1[0])+"_"+str_value1+"_2_"+str_value2
#                 #if coming from value2 The value exist in the file is  V1_num[1]_1_v2
#                 file2 = str(jeffdean1[0])+"_"+str_value2+"_2_"+str_value1
#                 file3 = file1+"__"+str_value1+"_"+str_value2+"_1_"+str(jeffdean1[0])
#                 file4 = file2+"__"+str_value1+"_"+str_value2+"_2_"+str(jeffdean1[0])
#                 file1 = path_folder + "/" + file1 + ".txt"
#                 file2 = path_folder + "/" + file2 + ".txt"
#                 file3 = path_folder + "/" + file3 + ".txt"
#                 file4 = path_folder + "/" + file4 + ".txt"
#
#                 xor_and_write(file1, file2, file3, file4, str_value1, str_value2)
#
# '''
