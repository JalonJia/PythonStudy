'''
Created on 2018年11月18日
文件基础操作
@author: JALON
'''

import os

#得到当前目录
cur_dir = os.getcwd()

print(cur_dir)

b_exist = os.path.exists('test.txt')
print(b_exist)

b_exist = os.path.exists('20181118.py')
print(b_exist)

b_isfolder = os.path.isdir('20181118.py')
print(b_isfolder)

b_isfile = os.path.isfile('20181118.py')
print(b_isfile)

print(os.listdir(cur_dir))

s_w_to = 'test.txt'
fout = open(s_w_to, 'w')
for i in range(1, 4):
    s_line = f'这是第{i}行\n'
    fout.write(s_line)

fout.close()

fin = open(s_w_to, 'r')
s_text = fin.read()
print(s_text)

fin.close()

#with方式打开文件不需要关闭
#第一种写法with codecs.open(s_file, 'r', 'UTF-8') as f: #调用转码
with open(s_w_to, 'r', errors='ignore' ) as f:
    #print(f.read())
    #逐行读取
    for word in f.readlines():
        print(word)
    

