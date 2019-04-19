from lxml import html
import requests
import os
from progressbar import ProgressBar

dir = os.path.dirname(os.path.realpath(__file__))
# print(dir)
def get_referred_links(url):
    try:
        page = requests.get('http://' + url, timeout = 0.1)
        webpage = html.fromstring(page.content)
        links = webpage.xpath('//a/@href')
        # print("Requesting " + url)
        return links
    except:
        return None

    # print(links)

def get_referring_links(url):
    pbar = ProgressBar()
    res = set()
    url = 'http://' + url
    with open(dir + '/res.txt', 'r') as file:
        links = file.readlines()
        for link in pbar(links):
            req_link = str(link.strip())
            referred_links = get_referred_links(req_link)
            if referred_links and url in referred_links:
                res.add(req_link)
            else:
                continue
        print("res :", str(res))
    return list(res)

if __name__ == '__main__':
    print(get_referring_links('uci.edu'))
    # out = get_referred_links('uci.edu')
    # for line in out:
    #     print(line)
# def get_refeering_links(url):

