"""
读取文件，随机显示一个字出来
"""

import os
import os.path
import glob #通配符
import tempfile #文件缓存
import linecache
#from linecache_data import *
import codecs #打开其他编码的文件
import random #随机数

#def open_charfile():
#    f = open(os.curdir + '/一年级语文生字.txt', 'rw')

print(os.curdir)
print(os.path.abspath(os.curdir))

#查看当前目录所有文件
for name in glob.glob(os.curdir + '/*'):
    print(name)

#查看当前目录所有文件，包含子目录
for name in glob.glob(os.pardir + '/*/*'):
    print(name)

s_file = os.curdir + '/一年级语文生字.txt'
for i in range(3):
    print(linecache.getline(s_file, i+1))

char_set = []
#with方式打开文件不需要关闭
#第一种写法with codecs.open(s_file, 'r', 'UTF-8') as f: #调用转码
with open(s_file, 'r', encoding='UTF-8', errors='ignore' ) as f:
    #print(f.read())
    for char in f.read():
        if char != '\n':
            print(char)
            char_set.append(char)
            
print(char_set)
print(len(char_set))       
for i in range(10):
    print(char_set[random.randint(0, len(char_set)-1)])
    
            

