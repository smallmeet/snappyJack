#!/usr/bin/python
# coding=utf-8
import urllib2
import json
import re

f = open('cms.txt', 'w')
try:
    for page in range(2):
    # for page in range(27):
        req = urllib2.Request('http://www.bugscan.net/common/2335/replies/?page='+str(page+1))
        res = urllib2.urlopen(req)
        json_res = json.loads(res.read())

        for i in json_res['results']:
            if re.search('\'.*\'.*:\[.*(\n.*)*\]|\".*\".*:\[.*(\n.*)*\]', i['content'].encode('UTF-8'), re.M):
                print re.search('\'.*\'.*:\[.*(\n.*)*\]|\".*\".*:\[.*(\n.*)*\]', i['content'].encode('UTF-8'), re.M).group().replace('\r\n','')
                f.write(re.search('\'.*\'.*:\[.*(\n.*)*\]|\".*\".*:\[.*(\n.*)*\]', i['content'].encode('UTF-8'), re.M).group().replace('\r\n','').replace('	','')+'\n')
except:
    print
