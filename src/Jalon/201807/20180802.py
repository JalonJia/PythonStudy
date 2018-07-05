'''
作业:
写一个函数 count_substr(s_source, s_sub), 返回字符串s_source中出现s_sub的次数。例如：调用时按以下参数调用：
i_count = count_substr('贾继开贾淼淼李娜贾彦龙', '贾'), i_count将会得到’贾’在前面字符串中出现的次数, 也就是得到结果3.
参数s_source传入源字符串，s_sub传入要查找的字符串，返回s_sub出现的次数。
'''

def count_substr(s_source, s_sub):
    i_count = 0
    i_len_sub = len(s_sub)
    i = 0
    while i < len(s_source):
        if s_source[i:i+i_len_sub] == s_sub:
            i_count += 1
            i += i_len_sub
            continue
        
        i += 1
                
    print(f'\'{s_sub}\'在\'{s_source}\'中出现了{i_count}次.')
    return i_count

count_substr('贾继开贾淼淼李娜贾彦龙', '贾')
count_substr('贾' * 10, '贾贾')


def calc_average(list_a):
    total = 0
    if len(list_a) == 0:
        return 0
    
    for x in list_a:
        total += x
    ret_val = total/len(list_a)
    print(f'{list_a}的平均值是：{ret_val}')
    return ret_val

calc_average([1,2,3,4,5,6,7,8,9,10])    
    
    