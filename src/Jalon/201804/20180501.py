'''
Created on 2018年5月1日

@author: Jalon
'''

'''
TODO: 2018-4-22周作业
练习6-3
回文时一个正向和逆向拼写都相同的单词，例如：'noon', 'a', 'redivider', 'bob'等。
作业1：编写一个函数is_palindrome, 接受一个字符串形参，如果这个字符串是回文，返回True，否则返回False。
作业2：编写完作业1之后，再编写一个函数check_palindrome，接受用户的输入，判断告诉用户输入的单词是否是回文。用户可以输入exit退出程序。
作业3：观看桌面上的’视频‘文件夹里面的视频，1-20，至少看到12.

提示：字符串可以使用[下标]取出每一个字符，len(str)函数可以返回字符串的长度。
'''

def is_palindrome(s):
    l = len(s)
    half_len = int(l / 2)
    for i in range(half_len):
        if s[i] != s[l - i - 1]:
            print('字符串%s不是回文' % s)
            return False
    
    print('字符串%s是回文' % s)
    return True



if __name__ == '__main__':
    s = 'axaa'
    is_palindrome(s)
    
    