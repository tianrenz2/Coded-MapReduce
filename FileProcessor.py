import os
from BinaryTool import BinaryTool
import shutil
import math
import random
import multiprocessing
############### Part 3  ##################
############# File name Changing  ##############

class FileProcessor(object):
    def __init__(self, file_dir, user_num, num_of_links,path):
        # dir = os.path.dirname(os.path.realpath(__file__))
        self.file_dir = file_dir
        self.user_num = user_num
        self.num_of_links=num_of_links
        self.longest_data = 0
        self.pair_dir = file_dir + "pair_dir/"
        self.max_len = 0
        self.path=path
        #print(self.user_num)
        #print(self.file_dir)
        
    def file_filling(self):
        loop_file=self.user_num*(self.user_num-1)
        mod_res=loop_file - self.num_of_links%loop_file
        #print("mod_res:", mod_res)
        if mod_res:
            for i in range(mod_res):
                with open(self.file_dir+str(i+1+self.num_of_links)+".txt","w") as file:
                    file.write("")

    def index_value(self):
        i = 1
        res = None
        files =os.listdir(self.file_dir)
        last_value=len(files)
        loop=last_value/(self.user_num*(self.user_num-1))
        return last_value,loop
    
    def rename(self):
        files=os.listdir(self.file_dir)
        for file_name in files:
            alpha, beta = self.index2pair(int(file_name.split('.')[0]))
            file_alpha=str(alpha+1)
            file_beta=str(beta+1)
            self.rename_file(file_name, str(file_alpha+"_"+file_beta+"_"+file_name))

    #os.rename(src, dst)
    def index2pair(self, index):
        var = self.user_num * (self.user_num - 1)
        x = index % var
        alpha = int(x / (self.user_num - 1))
        t = x % (self.user_num - 1)
        beta = t if t < alpha else t + 1
        return alpha, beta
                             
    def pair2index(self, alpha, beta):
        if alpha<beta:
            index=alpha*(self.user_num -1)+beta
        else:
            index=alpha*(self.user_num -1)+(beta-1)
        return

    def process_file(self, file_name):
        name_list = file_name.split('.')
        index = name_list[0]
        alpha, beta = self.index2pair(int(index))
        new_name = str(alpha) + '_' + str(beta) + '_' + index
        ret = self.rename_file(file_name, new_name + ".txt")
        if ret:
            return True
        else:
            return False

    def rename_file(self, file_name, new_name):
        # files= os.listdir(self.file_dir)
        try:
            os.rename(self.file_dir + file_name, self.file_dir + new_name)
            return True
        except:
            return False


    def create_pair_files(self, dir_name,users):#step 4
        running_user = str(users)
        print(running_user)
        if not os.path.isdir(self.path + "coded_"+running_user+'/'+dir_name + '/'):
            os.mkdir(self.path + "coded_"+running_user+'/'+dir_name + '/')
        write_dir = self.path + "coded_"+running_user+'/'+dir_name + '/'
        self.pair_dir = write_dir
        print("writting to " + write_dir)
        files = os.listdir(self.file_dir)
        for file_name in files:
           print(file_name)
           parameter_list = file_name.split('.')[0].split('_')
           if len(parameter_list) < 3:
               continue
           # print(file_name.split('.')[0].split('_'))
           alpha, beta, index = parameter_list
           # alpha, beta, index = int(alpha), int(beta), int(index)
           with open(self.file_dir  + '/' + file_name) as f:
               links = f.readlines()
               if not links:
                   continue
               source = links[0].strip()
               links = links[1:]
               if not links:
                   self.write_file(alpha, beta, "", source, write_dir)
               written_data = []
               counter = 0

               for link in links:
                   link = link.strip()
                   self.write_file(alpha, beta, link, source, write_dir)
               # print("Source "  + file_name + " has been written successfully")


    def write_file(self, alpha, beta, link, source, write_dir):
        if not link:
            gamma = str(self.user_num)
        #print("lonely link:",source)
        else:
            gamma = str((int(link) % self.user_num + 1))
        if int(alpha) < int(beta):
            alpha_beta = alpha + '_' + beta
            theta = '1'
        else:
            alpha_beta = beta + '_' + alpha
            theta = '2'
        new_file_name = write_dir + alpha_beta + '_' + theta + '_' + gamma + '.txt'
        op = 'w' if not os.path.exists(new_file_name) else 'a'
        print("writing directory",write_dir)
        with open(new_file_name, op) as f2:
            written_data = '(' + link + ',' + source + ')' + '\n'
            # print(new_file_name + ", " +written_data)
            f2.write(written_data)
            # return len(written_data)

    def find_largest(self):
        if not self.pair_dir:
            print(self.pair_dir)
            raise Exception("You have not created pairs yet")
        files = os.listdir(self.pair_dir)
        max_len = 0
        for file_name in files:
            if not os.path.isfile(self.pair_dir + file_name):
                continue
            with open(self.pair_dir + file_name, 'r') as f:
                try:
                    s = f.read()
                    if len(s) > max_len:
                        max_len = len(s)
                except:
                    print(s)
        return max_len

    # def align_bits(self, bits):
    #     if not self.max_len:
    #         raise Exception("There is no max file yet")
    #     bits_list = bits.split(' ')
    #     if len(bits_list) == self.max_len:
    #         return bits
    #     return ' '.join(bits_list + ['0'* 7] * (self.max_len - len(bits_list)))

    def write_bin_files(self):
        files = os.listdir(self.pair_dir)
        write_dir = self.pair_dir + 'bin_dir/'
        if not os.path.isdir(write_dir):
            os.mkdir(write_dir)

        binary_tool = BinaryTool(self.pair_dir)
        for file in files:
            if not os.path.isfile(self.pair_dir + file) or file.split('.')[1] != 'txt':
                continue
            bits = binary_tool.encrypt(file)
            # aligned_bits = self.align_bits(bits)#can be comment
            # print("aligned bits", len(aligned_bits))
            with open(write_dir + file, 'w') as f:
                f.write(bits)

    def file_mapping(self):
        new_path=self.file_dir
        files=os.listdir(new_path)
        results=set()
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
        for folder_name in results:#delete folders that exists from previous run
            folder_name=folder_name+"/original"
            if os.path.exists(self.path+ folder_name):
                shutil.rmtree(self.path+ folder_name)
        for folder_name in results:#create new folders for the number desired
            if os.path.isdir(self.path):
                folder_name=folder_name+"/original"
                os.mkdir(os.path.join(self.path, folder_name))
        counter=0
        users=[]
        users=[value+1 for value in range(self.user_num) if value <self.user_num]
        for files_names in files:
            files_name=files_names.split('.')
            file_name=files_name[0].split('_')
            if len(files_names) > 4:
                first="coded_"+file_name[0]
                third="coded_"+file_name[1]
                shutil.copy(new_path+files_names, self.path+first+"/original/")
                shutil.copy(new_path+files_names, self.path+third+"/original/")
        return results,number_result,users
    
    def file_changes(self,dir_name,users):
        # pool=multiprocessing.Pool(processes = self.user_num)
        jobs = []
        for i in users:
            print("Current modify the user"+ str(i))
            p = multiprocessing.Process(target=self.create_pair_files, args=('pair_dir', i,))
            jobs.append(p)
            p.start()
            # pool.apply_async(self.create_pair_files, [i])
        # pool.close()
        # pool.join()

if __name__ == "__main__":
    fp = FileProcessor( "coded_master/", 4, 1155)
    # fp.create_pair_files("pair_dir")
    fp.max_len = fp.find_largest()
    fp.write_bin_files()
    # print(fp.process_file("1.txt"))

