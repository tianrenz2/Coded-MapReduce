import os
import shutil
import multiprocessing
import math
import random
import time,datetime
import multiprocessing
from BinaryTool import  BinaryTool

class FileReduce(object):
    def __init__(self, users, folder_path,path):
        #self.file_dir = file_dir
        self.users = users
        self.folder_path=folder_path
        self.path=path

    def reduce(self, value):
        def get_pair(a, b):
            return str(a) + '_' + str(b) if a < b else str(b) + '_' + str(a)

        reducer_id = value[0]
        combinations = value[1]
        binary_tool = BinaryTool("")
        read_path = self.path + "coded_" + str(reducer_id) + '/'

        print("Reducer id:", reducer_id)
        files_to_read = set()
        for theta in ['1', '2']:
            for comb in combinations:
                alpha, beta = comb[1], comb[2]
                new_comb_1 = get_pair(alpha, beta)
                new_comb_2 = get_pair(int(reducer_id), alpha)
                new_comb_3 = get_pair(int(reducer_id), beta)
                files_to_read.add(new_comb_1 + '_' + theta + '_' + str(reducer_id))
                files_to_read.add(new_comb_2 + '_' + theta + '_' + str(reducer_id))
                files_to_read.add(new_comb_3 + '_' + theta + '_' + str(reducer_id))

        print(list(files_to_read))
        print("\n")
        file_to_write =  self.path + "coded_" + str(reducer_id) + '/' + "output.txt"
        mem = {}
        for file in list(files_to_read):
            with open(read_path + file + ".txt", 'r') as f:
                content = binary_tool.decrypt(f.read())
                content = content.split('\n')
                written_data = ""
                source = -1
                target = -1
                for line in content:
                    line = line[:line.find('\x01')]
                    pair = line[1 : -1].split(',')
                    if len(pair) == 2:
                        if pair[0]:
                            target = int(pair[0])
                        if pair[1]:
                            source = int(pair[1])
                    new_form = (source, target)
                    print(new_form)
                    if new_form in mem:
                        mem[new_form] += 1
                    else:
                        mem[new_form] = 1

        pair_list = []
        for key in mem.keys():
            if(key[0] < 0 and key[1] < 0):
                continue
            pair_list.append((key[0], key[1], mem[key]))

        pair_list = sorted(sorted(sorted(pair_list, key = lambda x: x[2]), key = lambda x: x[1]), key = lambda x: x[0])

        for pair in pair_list:
            op = 'a'
            if not os.path.isfile(file_to_write):
                op = 'w'
            written_data = '(' + str(pair[0]) + ',' + str(pair[1]) + ')' + str(pair[2]) + '\n'
            with open(file_to_write, op) as wf:
                wf.write(written_data)


                # with open(file_to_write, op) as write_file:
                #     write_file.write(orig_content)



# if __name__ == "__main__":
#     fr = FileReduce(4, )