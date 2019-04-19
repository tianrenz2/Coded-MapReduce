import timeit
import sys
import os
import numpy as np
import pandas as pd
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
import os
from Crawler import Crawler
from FileProcessor import FileProcessor
from FileTransfer import FileTransfer
from FileCodedTransfer import FileCodedTransfer
from FileReduce import FileReduce

dir = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    path = ROOT_DIR+'/'
    # path="/Users/xiaoran/Dropbox/Reverse_Index/"
    # folder_path="/Users/xiaoran/Dropbox/Reverse_Index/coded_master"

    folder_path = path + 'coded_master/'
    def moveFileto(sourceDir,  targetDir):
        shutil.copy(sourceDir,  targetDir)
    print("How many user you are trying to have?")
    users=input()
    user = int(users)
    print("you are going to have " +users + " users for this simulation" )
    reinit = False

    remapping = True
    # # file_transfer=FileTransfer(users,folder_path,path)
    # # result, number_result = file_transfer.Mapping()
    # file_coded_transfer=FileCodedTransfer(users,folder_path,path)
    # everything=file_coded_transfer.shufgen()
    # #    file_transfer.Call_naive_function(everything)
    # file_coded_transfer.Call_coded_function(everything)


#
#    ##reduce
#    file_reduce=FileReduce(users,folder_path,path)
#    file_reduce.file_name_seeking()

    if reinit:
        if os.path.exists(folder_path):  # Delete the folder if the folder exist
            shutil.rmtree(folder_path)
        # def filecreating():
        files = os.listdir(path)  # get file name under the folder
        # define the access rights
        access_rights = 0o755
        try:
            os.mkdir(folder_path, access_rights)
        except OSError:
            print("Creation of the directory %s failed" % folder_path)
        else:
            print("Successfully created the directory %s" % folder_path)
        for folder_nameint in range(user):  # delete folders that exists from previous run
            folder_name = str(folder_nameint + 1)
            if os.path.exists(os.path.join(path, "coded_" + folder_name)):
                shutil.rmtree(os.path.join(path, "coded_" + folder_name))

        for folder_nameint in range(user):  # create new folders for the number desired
            folder_name = str(folder_nameint + 1)
            if os.path.isdir(path):
                os.mkdir(os.path.join(path, "coded_" + folder_name))
        linkdict = {}
        reverse_linkdict = {}
        with open(dir + "/res.txt", "r") as f:
            links = f.readlines()
            num_of_links = len(links)
            linkdict = {value + 1: links[value].strip() for value in range(num_of_links)}
            reverse_linkdict = {links[value].strip(): value + 1 for value in range(num_of_links)}

        # print(reverse_linkdict)
        os.chdir(folder_path)  # change the director for the folder path

        # Created an instance of crawler and pass user number and links file into
        crawler = Crawler(user, "res.txt", reverse_linkdict, linkdict)
        # #Call crawl_and_createfile method to get all target links and create file for each source link
        crawler.crawl_and_createfile();

        fileprocess = FileProcessor(folder_path, user, num_of_links)
        fileprocess.file_filling()
        fileprocess.index_value()
        #    fileprocess.index2pair()
        fileprocess.rename()
        # rename()
        fileprocess.create_pair_files('pair_dir')
        # if need for shuffle and reduce file

        fileprocess.max_len = fileprocess.find_largest()
        fileprocess.write_bin_files()

    if remapping:
        file_transfer=FileTransfer(users,folder_path,path)
        result, number_result = file_transfer.Mapping()

        file_coded_transfer = FileCodedTransfer(users, folder_path, path)
        everything=file_coded_transfer.shufgen()
        print("everything", everything)
        # file_transfer.Call_naive_function(everything)
        file_coded_transfer.Call_coded_function(everything)
        fr = FileReduce(users, folder_path, path)
        for val in everything:
            fr.reduce(val)