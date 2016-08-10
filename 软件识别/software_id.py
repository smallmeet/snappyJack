#!usr/bin/python
# coding=utf-8
import hashlib
import re
import urllib
import urllib2
import threading

f = open('cms.txt', 'r')
# host = 'http://www.xlcolor.cn/'       #shop7z 测试
# host = 'http://mail.szjhqh.com/'       # szjhqh测试
# host = 'http://119.145.194.122:9090/' + '/'
# host = 'http://ecard.sdwz.cn' + '/'
# host = 'http://www.szfcsc.com/' + '/'
# host = 'http://fsd2014.f3322.org:9090/' + '/'
# host = 'http://jmll2zx.com:1016/' + '/'
host = 'http://www.cnfia.cn' + '/'

res_md5 = None

def div_list(ls, n):                                         #拆分list
    if not isinstance(ls, list) or not isinstance(n, int):
        return []
    ls_len = len(ls)
    if n <= 0 or 0 == ls_len:
        return []
    if n > ls_len:
        return []
    elif n == ls_len:
        return [[i] for i in ls]
    else:
        j = ls_len / n
        ls_return = []
        for i in xrange(0, (n - 1) * j, j):
            ls_return.append(ls[i:i + j])
        ls_return.append(ls[(n - 1) * j:])
        return ls_return

def get_res_txt(host, url):  # 输入url 返回源码
    req = urllib2.Request(host + url)
    if urllib.urlopen(host + url).code == 200:
        response = urllib2.urlopen(req)
        return response.read()
    else:
        return None


def get_res_pic(host, url_title):  # 输入url 判断状态码，并返回md5
    req = urllib2.Request(host + url_title)
    if urllib.urlopen(host + url_title).code == 200:
        response = urllib2.urlopen(req, timeout=3)
        the_page = response.read()
        m2 = hashlib.md5()
        m2.update(the_page)
        return m2.hexdigest()
    else:
        return None


def ident(f):                           #传入list，执行操作
    for line in f:  # 读取txt每一行
        line_title = line.split(':')[0].replace('\'', '').replace('"', '')  # title
        line_split = line.split(')')
        line_split.pop()
        left_part = re.compile('\(.*')
        for each_split in line_split:  # 每一个括号
            if left_part.findall(each_split).__len__() != 0:
                print line_title
                short_part = left_part.findall(each_split)[0].replace('\'', '').replace('"', '').replace('(', '')
                if re.search(',', short_part):
                    comma_split = short_part.split(',')  # 逗号分割的两部分
                    if re.search('.*(\.jpg|\.ico|\.gif|\.png).*', comma_split[0], re.M):  # 图片格式
                        res_md5 = get_res_pic(host, comma_split[0])
                        if res_md5 != None:
                            if res_md5 == comma_split[1]:
                                print '软件为    ' + line_title
                                continue
                    else:
                        if get_res_txt(host, comma_split[0]):
                            result_content = get_res_txt(host, comma_split[0])
                            if re.search(comma_split[1], result_content, re.M):
                                print '软件为  ', line_title
                                continue


split_list=div_list(f.readlines(),5)        #拆分cms.txt
for i in range(5):
    t1=threading.Thread(target=ident,args=(split_list[i],))
    t1.start()
