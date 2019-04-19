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
from lxml import html
import requests
import os
from progressbar import ProgressBar


dir = os.path.dirname(os.path.realpath(__file__))
src_tar_map = {}

# print(dir)
def source_links(url):#source
    try:
        print("Processing " + url)
        page = requests.get('http://' + url, timeout=0.1)
        webpage = html.fromstring(page.content)
        links = webpage.xpath('//a/@href')
        # print("Requesting " + url)
        return links
    except:
        return None

# print(links)

def target_links(url): #target
    pbar = ProgressBar()
    res = set()
    url = 'http://' + url
    with open(dir + '/res.txt', 'r') as file:
        links = file.readlines()
        for link in pbar(links):
            req_link = str(link.strip())
            referred_links = source_links(req_link)
            if link not in src_tar_map.keys():
                src_tar_map[link] = referred_links
            if referred_links and url in referred_links:
                res.add(req_link)
            else:
                continue
        print("res :", str(res))
    return list(res)


############### Part 2  ##################
############# File Creating  ##############

def sratch(user):
    num_of_files = user*user*(user-1)
    # num_of_links = 1000
    link_id = 0
    finished = False
    with open(dir + "/res.txt", "r") as f:
        links = f.readlines()
        num_of_links = len(links)


        num_of_link_upperbound = math.ceil(num_of_links/num_of_files) * num_of_files
        print("ceil", num_of_link_upperbound)
        while link_id <= num_of_link_upperbound:
            for alpha in range(1, user):
                for delta in range(alpha + 1, user + 1):
                    for gamma in [1, 2]:
                        for theta in range(1, user + 1):
                            if link_id >= num_of_link_upperbound:
                                return
                            targets = None
                            link = None
                            if(link_id < num_of_links):
                                link = links[link_id].strip()
                                targets = source_links(link)
                            else:
                                links = None
                            print(str(alpha) + '_' + str(delta) + '_' + str(gamma) + '_' + str(link_id), "link",
                                      link, "targets", targets)
                            link_id += 1
                            with open("master/" + str(alpha) + '_' + str(delta) + '_' + str(gamma) + '_' + str(link_id) + ".txt", 'w') as f:
                                if link:
                                    f.write(link + '\n')
                                if targets:
                                    for target in targets:
                                        if len(target) > 4 and target[:4] == 'http':
                                            f.write(target + '\n')


'''
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
print(results)
print(number_result)
#print(type(file_name))

return (results,number_result)
'''





if __name__ == '__main__':
    print("How many user you are trying to have?")
    users=input()
    user = int(users)
    sratch(user)