'''
Created on 2018年5月30日
@todo: 正则表达式的使用
@author: jalon
'''

import re

def check_match(s_regx, s_source):
    result = re.match(s_regx, s_source)
    if result != None :
        print('%s匹配%s的结果是: ' % (s_source, s_regx), result.group())
    else:
        print('%s与%s不匹配' % (s_source, s_regx))
    
def test():
    s = '12345 abcdefg'
    list_regx = ['123*', '.', '[a-z,0-9]', '\d', '\D', '\s', '\S', '\w', '\W',
                 '\d\s\d'
                 ]
    #'.'匹配一个字符,\n除外
    #'[]'匹配列举的字符, 
    #[^123]^表示取反,Not In后面的字符
    #[a-z]表示a到z
    #'\d' 数字, 等同于[0-9]
    #'\D' 非数字, 等同于[^0-9]
    #'\s' 空白, 包括空格和Tab
    #'\S', 非空白
    #'\w', a-z,A-Z,0-9,_ , 等同于[a-zA-Z0-9_]
    #'\W' 非单词字符
    #可以自由组合,例如'\d\s\d'表示数字开头,第二位是空白
    
    for regx in list_regx:
        check_match(regx, s)
       
    '''
            数量单位:
            * 前一个字符出现>=0次
            + 前一个字符出现>=1次
            ? 前一个字符出现0或1次
            {m} 前一个字符出现m次
            {m,} 前一个字符出现>=m次
            {m,} 前一个字符出现>=m次<=n次
    '''
    s = '12345 abcdefg'
    #s = '12345 '
    list_regx = ['123\d*', '\d+\s[a-z]*', '\d+\s[a-z]+', '\d?', '\d?[a-z]+',
                 '\d{3} [a-z]+', '\d{5} [a-z]+',
                 ]
    for regx in list_regx:
        check_match(regx, s)
    


if __name__ == '__main__':
    test()
    
    