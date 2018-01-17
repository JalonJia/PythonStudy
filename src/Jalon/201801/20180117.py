"""
文件路径操作
"""

import os
import os.path

for root, dirs, files in os.walk('D:\Test'): #files会得到目录下的文件（不包括文件夹）；dirs会获取到每个文件夹下面的子目录；root会遍历每个子文件夹
    print(root, "consumes", end="")
    print(files)
    print(dirs)
    #print(sum([os.path.getsize(join(root, name)) for name in files]), end="")
    #print("bytes in", len(files), "non-directory files")
    #if 'CVS' in dirs:
    #    dirs.remove('CVS')  # don't visit CVS directories

#定位到文件夹
os.chdir('C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE')
#执行命令
fp = os.popen('vb7to8.exe /help')
fpread = fp.read()
print(fpread)
    