#coding=utf-8
from PIL import Image
import argparse

ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    gray=int(0.2126*r+0.7125*g+0.0722*b) #灰度值计算
    return 70*gray/257  #70为字符串长度
imgfile=Image.open('ascii_dora.png')
# print imgfile.width
# print imgfile.height
pix= imgfile.load()
# print pix[0,0]#获得像素点的rbg
pix[0,0]=(1,255,255,0)
# print pix[0,0]#获得像素点的rbg
for i in range(imgfile.width):
    print pix[40,i]
