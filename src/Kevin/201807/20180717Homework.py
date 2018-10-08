'''
Created on 2018年7月17日
作业: 关于字符串的一些计算
1. 写一个函数find(str, substr), 传入一个string str以及一另一个字符串substr，函数用来判断字符串str中是否包含字符串substr，
        如果包含，打印结果并返回substr在字符串str中的下标；如果不包含，返回-1
2. 写一个函数count(str, substr), 传入一个string str以及一另一个字符串substr，函数用来计算并返回字符串str中包含字符串substr的次数，
       
3. 写一个函数replace(str, substr, substr2), 传入三个字符串，函数将第一个字符串str中的子字符串substr都替换成substr2, 并返回替换后的字符串.
 例如：调用s = replace('jiajikai jiamiaomiao jiayanlong', 'jia', 'j_')之后，s的值是'j_jikai j_miaomiao j_yanlong'
4. 写一个函数get_chars(str), 传入一个字符串str, 返回字符串中包含的所有不重复的字符列表。
例如：调用 x = get_chars('jiajikai')之后，x是这样的列表：['j','i','a','k'](包含了字符串的所有字母，并且不重复）。提示：调用上次写的函数。

5. 练习10-6
    两个单词，如果重新排列其中一个的字母可以得到另一个，则它们互为回文。写一个函数is_angaram(str1, str2)传入两个字符串，当它们互为回文时返回True，否则返回False。
    例如：is_angaram('abc', 'cba')会返回True; is_angaram('xbc', 'cba')会返回False。

'''

def find(str, substr):
    t = 0
    u = 0
    if len(substr) > len(str):
        print(f'字符串{str}中不包含字符串{substr}')
        return -1
    
    h = len(substr)

    for i in range(len(str)):
        if str[t:h] == substr:
            u += 1
        h += 1
        t += 1
        
    if u > 0:
        print(f'字符串{str}中包含字符串{substr}')
        print(f'{substr}在{str}中出现的次数是{u}')
        return u
    else:
        print(f'字符串{str}中不包含字符串{substr}')
        print(f'{substr}在{str}中出现的次数是{u}')
        return -1
find(str = ('fg'), substr = 'fg')
'''
    u = 0
    for i in str:
        if i == substr:
            u += 1
    if u > 0:
        print(f'字符串{str}中包含字符串{substr}')
    else:
        print(f'字符串{str}中不包含字符串{substr}')
    print(f'{substr}在{str}中出现的次数是{u}')
'''

def count(str, substr):
    if len(substr) > len(str):
        print('出现的次数是0')
        return
    t = 0
    u = 0
    h = len(substr)

    for i in range(len(str)):
        if str[t:h] == substr:
            u += 1
        h += 1
        t += 1
    print()
    print(f'{substr}在{str}中出现的次数是{u}')


count(str = (''), substr = 'h')