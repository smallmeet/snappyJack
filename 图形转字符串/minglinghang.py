#coding=utf-8
#获取命令行和脚本名
import sys
print "脚本名：", sys.argv[0]
for i in range(1, len(sys.argv)):
    print "参数", i, sys.argv[i]
