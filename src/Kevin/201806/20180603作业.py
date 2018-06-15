'''
作业:
写一个函数 count_substr(s_source, s_sub), 返回字符串s_source中出现s_sub的次数。例如：调用时按以下参数调用：
i_count = count_substr('贾继开贾淼淼李娜贾彦龙', '贾'), i_count将会得到’贾’在前面字符串中出现的次数, 也就是得到结果3.
参数s_source传入源字符串，s_sub传入要查找的字符串，返回s_sub出现的次数。
'''
from test.test_binop import isnum

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(len(y)):
    if isnum(y[x]):
        y[x] += 100
    print(y[x])
    y[x] -= 100
print(y)

  