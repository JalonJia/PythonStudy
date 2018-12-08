'''
Created on 2018年11月18日

文件读写
@author: KKVV
'''

#第一种方式，使用open打开文件，然后要使用close关闭文件
f = open('test.txt', 'w')
s_content = '第1行内容\n'
f.write(s_content)

f.close()


#文件读取
f = open('test.txt', 'r')
s_content = f.read()
print(s_content)

f.close()


#另一种打开文件的方式，打开之后不需要关闭，with程序结束时会自动关闭文件
s_w_to = 'test.txt'
with open(s_w_to, 'w', encoding='UTF-8', errors='ignore' ) as f:
    for i in range(1, 4):
        f.write(f'第{i}行内容\n')


with open(s_w_to, 'r', encoding='UTF-8', errors='ignore' ) as f:
    i = 0
    for s in f.readlines():
        i += 1
        print(f'第{i}行： {s}')
        
#读取其他目录的文件 -- 相对路径
s_file = '../StudyTest/二年级英文单词.txt' #../表示上一级目录，./表示本目录
print('---------------------以下内容来自：', s_file, '--------------------------------')
with open(s_file, 'r', encoding='UTF-8', errors='ignore' ) as f:
    i = 0
#    for s in f.readlines():
#       i += 1
#       print(f'第{i}行： {s}')

    s_text = f.read()
    print(s_text)
    
#读取其他目录的文件 -- 绝对路径
s_file = 'C:\Dev\git\PythonStudy\src\Jalon\StudyTest\二年级英文单词.txt'
print('--------绝对路径-------------以下内容来自：', s_file, '--------------------------------')
with open(s_file, 'r', encoding='UTF-8', errors='ignore' ) as f:
    i = 0
#    for s in f.readlines():
#       i += 1
#       print(f'第{i}行： {s}')

    s_text = f.read()
    print(s_text)
    
    
    
