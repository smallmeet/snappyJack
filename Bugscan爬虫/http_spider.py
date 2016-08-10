#!/usr/bin/python
# coding=utf-8
import urllib2
import json
import re

f=open('cms_eg.txt','w')
for page in range(27):
    req = urllib2.Request('http://www.bugscan.net/common/2335/replies/?page=' + str(page + 1))
    res = urllib2.urlopen(req)
    json_res = json.loads(res.read())
    try:
        for i in json_res['results']:
            # print i['content'].encode('UTF-8')
            if re.search(':\[.*(\n.*)*\]', i['content'].encode('UTF-8'), re.M):
                name=re.search('\'.*\':', i['content'].encode('utf-8'), re.M).group()
                if re.search('http.*', i['content'].encode('UTF-8'), re.M):
                    pattern = re.compile("http.*")
                    http_lists= pattern.findall(i['content'].encode('utf-8'))
                    for http_list in http_lists:
                        print name+'|'+http_list
                        f.write(name+'|'+http_list+'\n')
    except:
        print

