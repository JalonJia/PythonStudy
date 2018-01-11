"""
文件路径操作
"""

import os
import os.path
from os.path import join #这样引入之后，join就可以直接使用了

#列出目录的文件
sPath = "D:\ACCPAC"
print(os.listdir(sPath))


print(os.path.split(sPath)) #将路径分解成两部分，第一部分从开始到最后一个路径分隔符，最后一个分隔符后面的路径
print(os.path.basename(sPath)) #路径的第二部分
print(os.path.dirname(sPath)) #路径的第一部分

sFile = "D:\\ACCPAC\\abcd.a.b.c"
print(os.path.splitext(sFile)) #将路径分解成两部分，第一部分从开始到最后一个文件后缀名，文件后缀名

listPath = os.listdir(sPath)
print(os.path.commonprefix(listPath)) #获取列表的公共部分

print(os.path.join(*listPath)) #将一个列表的内容连接起来，生成一个新路径。如果列表中的内容包含分隔符，只会连接最后一个分隔符之后的内容

#获取系统环境变量
print(os.environ['Path'])
print(os.environ['homepath'])
print(os.path.expandvars('C:/ZZZ/$homepath')) #expandvars中可以使用$环境变量替换内容
print(os.path.normpath(sFile)) #使用normpath去除多余的分隔符

print(os.curdir) #相对路径
print(os.pardir) #上一层路径
print(os.path.abspath(os.curdir)) #相对路径转绝对路径

sFile = os.path.join(os.curdir, '20180107.py')
print(sFile)
print(os.stat(sFile)) #文件属性列表

print(__file__) #当前文件
print(os.path.isdir(sPath)) #是否文件夹
print(os.path.isfile(sPath)) #是否文件
print(os.path.islink(sPath)) #是否快捷方式
print(os.path.exists(sFile)) #是否存在
print(os.path.isabs(sFile)) #是否绝对路径
print(os.path.isabs(os.path.abspath(sFile))) #是否绝对路径

sPath2 = 'D:\Test1\T2'
#os.mkdir(sPath2) #创建文件夹，只能一层一层创建

print(__name__)

#os.path.('D:\')

print(os.walk('D:\Test'))
#os.walk('D:\\', Null, Null, Null)
for root, dirs, files in os.walk('D:\Test'): #files会得到目录下的文件（不包括文件夹）；dirs会获取到每个文件夹下面的子目录；root会遍历每个子文件夹
    print(root, "consumes", end="")
    print(files)
    print(dirs)
    #print(sum([os.path.getsize(join(root, name)) for name in files]), end="")
    #print("bytes in", len(files), "non-directory files")
    #if 'CVS' in dirs:
    #    dirs.remove('CVS')  # don't visit CVS directories








