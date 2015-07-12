import os
import re
from optparse import OptionParser

import sys
dirpath = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.join(dirpath, 'newspaper')
sys.path.insert(0,parent_path)
#print(sys.path)

from HEDownloader import *
from HEConfig import *

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", default='')
    parser.add_option("-t", "--type", dest="type",default='')
    parser.add_option("-c", "--category", dest="category",default='')
    parser.add_option("-r", "--regex", dest="regex_for_links",default='')
    parser.add_option("-a", "--tags", dest="tags",default='')
    parser.add_option("-f", "--force", dest="force",default=False)
    (options, args) = parser.parse_args()
    (url,url_type,category,regex_for_links,tags) =(options.url,options.type,options.category,options.regex_for_links,options.tags)
    print("url:%s url_type:%s category:%s regex_for_links:%s tags:%s args:%s",url,url_type,category,regex_for_links,tags,args)

    if url == '' or url_type == '' or category == '':
        print("error, must input url,url_type,category")

    config = HEConfig();

    if url and url_type == 'article':
        downloadFile(url,category,config,'',tags)
    elif url and url_type == 'feed':
        downloadFeed(url,category,config,tags)
    elif url and url_type == 'articles':
        downloadArticles(url,category,config,regex_for_links,tags)
    else:
        print("do nothing\n")
        #downloadByConfig(urls,config,outputDir,max_number)
