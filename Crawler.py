# print(dir)
import requests
from progressbar import ProgressBar
from lxml import html
import os

class Crawler(object):
    def __init__(self, user, link_file, reverse_linkdict, linkdict):
        self.user = user
        self.link_file = link_file
        self.src_tar_map = {}
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.reverse_linkdict=reverse_linkdict
        self.linkdict = linkdict
    
    def source_links(self, url):#source
        # This method is to crawl all the target links for one source link
        try:
            #print("Processing " + url)
            page = requests.get('http://' + url, timeout=0.1)
            webpage = html.fromstring(page.content)
            links = webpage.xpath('//a/@href')
            # print("Requesting " + url)
            return links
        except:
            return None

    # print(links)

    def target_links(self, url): #target
        # This method is to crawl all the source links for one target links
        pbar = ProgressBar()
        res = set()
        url = 'http://' + url
        with open(dir + '/res.txt', 'r') as file:
            links = file.readlines()
            for link in pbar(links):
                req_link = str(link.strip())
                referred_links = self.source_links(req_link)
                if link not in self.src_tar_map.keys():
                    self.src_tar_map[link] = referred_links
                if referred_links and url in referred_links:
                    res.add(req_link)
                else:
                    continue
            #print("res :", str(res))
        return list(res)

    def create_file(self, link, link_id, targets):
        # This method is to create a file given the source link information and targets
        with open(str(link_id) + ".txt", 'w') as f:
            if link:
                f.write(str(self.reverse_linkdict[link]) + '\n')
                if targets:
                    for target in targets:
                        if len(target) > 4 and target[:7] == 'http://':
                            target_split = target.split("//")
                            if len(target_split) < 2:
                                continue
                            target = target_split[1]
                            if(target[-1] == '/'):
                                target = target[:-1]
                            write_data = None
                            if("www." + target in self.reverse_linkdict.keys()):
                                write_data = self.reverse_linkdict["www." + target]
                            elif(target in self.reverse_linkdict.keys()):
                                write_data = self.reverse_linkdict[target]
                            if not write_data:
                                new_index = len(self.reverse_linkdict.keys()) + 1
                                self.reverse_linkdict["www." + target] = new_index
                                write_data = self.reverse_linkdict["www." + target]
                                self.linkdict[new_index] = "www." + target
                            #print("target written", write_data)
                            f.write(str(write_data) + '\n')

    def crawl_and_createfile(self):
        # This method is to get all target links and create file for each source link
        num_of_files = self.user * self.user * (self.user-1)
        link_id = 0
        with open(self.dir + "/" + self.link_file, "r") as f:
            links = f.readlines()
            num_of_links = len(links)
            #print("ceil", num_of_link_upperbound)
            #print(num_of_links)
            while link_id < num_of_links:
                link = links[link_id].strip()
                targets = self.source_links(link)
                link_id += 1
                self.create_file(link, link_id, targets)
