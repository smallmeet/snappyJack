#!/usr/bin/python
# coding=utf-8

import urllib2
import cookielib
import time

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
data='''info={"username":"zhangzycn@foxmail.com","password":"3d8d1200d278df5664761922ff2cEHBQ","code":"","autologin":false}'''
# data = urllib.urlencode(data)

req = urllib2.Request("https://www.oshadan.com/validateLogin",data)
req.add_header('Host','www.oshadan.com')
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0')
req.add_header('Accept','application/json, text/javascript, */*; q=0.01')
req.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
req.add_header('Accept-Encoding','gzip, deflate, br')
req.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
req.add_header('X-Requested-With','XMLHttpRequest')
req.add_header('Referer','https://www.oshadan.com/login')
req.add_header('Content-Length','115')

content=opener.open(req)
print content.read()
# test=opener.open('https://www.oshadan.com/')
# print test.read()

keyword = 'port:8080'  # 获取查询关键字
page = '1'  # 获取页数
# f = open('result.txt', 'w')
# keyword = sys.argv[1]  # 获取查询关键字
# page = sys.argv[2]  # 获取页数
# get_cookie = sys.argv[3]  # 获取cookie的值
for i in range(int(page)):
    f_req=opener.open('https://www.oshadan.com:443/search?info={"c":"' + keyword + '","p":' + str(i + 1) + ',"q":0,"clear":false}&_='+str(time.time()).replace('.','')+'0')
    print f_req.read()






