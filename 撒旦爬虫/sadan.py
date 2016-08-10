#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
import urllib2
import sys

keyword = 'port:8080'  # 获取查询关键字
page = '1'  # 获取页数
f = open('result.txt', 'w')
# keyword = sys.argv[1]  # 获取查询关键字
# page = sys.argv[2]  # 获取页数
# get_cookie = sys.argv[3]  # 获取cookie的值
for i in range(int(page)):
    req = urllib2.Request('https://www.oshadan.com:443/search?info={"c":"' + keyword + '","p":' + str(i + 1) + ',"q":0,"clear":false}&_='+str(time.time()).replace('.','')+'0')
    req.add_header('Host', 'www.oshadan.com')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0')
    req.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    req.add_header('Referer', 'https://www.oshadan.com/main')
    req.add_header('Cookie', 'sid=s%3Abojn6UmMsWcvTlf97yWtsHLM.BWamQyVwpPz1L4JwelKJqgrEoK0JXqRZF1xy19EN7Co')
    # req.add_header('Cookie', get_cookie)
    response = urllib2.urlopen(req)
    the_page = response.read()
    json_re = json.loads(the_page)
    # print json_re['result']['result']['recordNum']  # 个数

    for j in json_re['result']['result']['data']:
        if j['notcomponentFields']['url'] != None:
            print j['notcomponentFields']['url']
            f.write(j['notcomponentFields']['url'])
            f.write('\n')
        else:
            print f.write(j['notcomponentFields']['ip'])
            f.write(j['notcomponentFields']['ip'])
            f.write(j['notcomponentFields']['port'])
            f.write('\n')
    print '第' + str(i + 1) + '页爬取完毕'
f.close()
print '爬虫任务全部结束'
