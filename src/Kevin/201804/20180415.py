

i_max = -1
list_input = []
s_input = ''

while s_input != 'end' :
    s_input = input("请输入一个数字，输入end时结束程序：")
    list_input.append(s_input)
    if s_input.isdigit() : 
        if i_max > int(s_input) :
            i_max = int(s_input)
        print("目前最小的数字是：%s" % i_max)
    elif s_input == 'end' :
        print("程序结束")
    else:
        print("无效输入，请输入一个数字，或者输入end结束程序。")

print("WHile循环结束，程序结束")
print("您刚才输入的内容有：%s" % list_input)

def is_triangles(d, j, e):
    if d > j + e:
        print('No')
    else:
        print('yes')
            
    if j > e + d:
        print('No')
    else:
        print('yes')

    if e > j + d:
        print('No')
    else:
        print('yes')

is_triangles(d = 12, j = 24, e = 1)        