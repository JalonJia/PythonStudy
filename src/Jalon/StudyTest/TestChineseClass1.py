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
import tkinter as tk
import copy



s_file = os.curdir + '/Temp.txt'
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
#print(len(char_set))       
#for i in range(10):
#    print(char_set[random.randint(0, len(char_set)-1)])

char_set_errors = []

class Application(tk.Frame):
    def __init__(self, char_set, char_set_errors, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.next_char = tk.Label(self, fg='blue', font='Consolas 100')
        self.next_char.pack(side="top")
        
        self.char_cnt = tk.Label(self, font='Consolas 12')
        self.char_cnt.pack()
        
        self.hi_there = tk.Button(self, font='Consolas 30')
        self.hi_there["text"] = "下一个"
        self.hi_there["command"] = self.read_next_char
        self.hi_there.pack(side="left")        

        self.list_round2 = tk.Button(self, font='Consolas 30')
        self.list_round2["text"] = "不认识"
        self.list_round2["command"] = self.char_to_nextround
        self.list_round2.pack(side="right")

        self.next_round = tk.Button(self, font='Consolas 30')
        self.next_round["text"] = "重置"
        self.next_round["command"] = self.read_next_round
        self.next_round.pack()        

        self.quit = tk.Button(self, text="退出", fg="red", font='Consolas 30',
                              command=root.destroy)
        self.quit.pack()

    def read_next_char(self):
        print(char_set)
            
        self.char_cnt["text"] = "剩余%s" % len(char_set)
        if len(char_set) > 0:
            i_this = random.randint(0, len(char_set)-1)
            self.next_char["text"] = char_set[i_this]
            char_set.remove(char_set[i_this])
        else:
            self.next_char["text"] = "恭喜，已完成测试！"
        #print("hi there, everyone!")

    def char_to_nextround(self):
        char_set_errors.append(self.next_char["text"])
        self.read_next_char()

    def read_next_round(self):        
        #char_set = copy.copy(char_set_errors)
        print('不认识:%s' % char_set_errors)
        for char in char_set_errors:
            char_set.append(char)        
        print(char_set)
        char_set_errors.clear()


root = tk.Tk()
app = Application(char_set, char_set_errors, master=root)
app.mainloop()

#form = tk.Tk()



