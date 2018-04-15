

'''
TODO: 让用户输入一些数字，并实时告诉他这些数字里最大的数是多少
当用户输入end时结束程序
'''
from test.test_binop import isnum

#
i_max = 0
list_input = []
s_input = ''

while s_input != 'end' :
    s_input = input("请输入一个数字，输入end时结束程序：")
    list_input.append(s_input)
    if s_input.isdigit() : #判断字符串是不是只有数字
        if i_max < int(s_input) :
            i_max = int(s_input)
        print("目前最大的数字是：%s" % i_max)
    elif s_input == 'end' :
        print("程序结束")
    else:
        print("无效输入，请输入一个数字，或者输入end结束程序。")

print("WHile循环结束，程序结束")
print("您刚才输入的内容有：%s" % list_input)


