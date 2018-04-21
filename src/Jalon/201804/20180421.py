'''
TODO: 让用户输入4个数字，然后判断这四个数字能不能组成一个长方形
如果能组成，把长方形画出来
否则，告诉用户不能组成长方形
'''

list_input = [] #列表用来存储用户输入的四个数字
s_input = '' #用来接受用户每次的输入，如果是数字，才放到list_input列表中
i_num_count = 0 #现在已经有几个合法的数字了
i_temp = 0

while i_num_count < 4:
    s_input = input("请输入第%d个数字：" % (i_num_count + 1))
    if s_input.isdigit():
        i_temp = int(s_input)
        list_input.append(i_temp)
        i_num_count += 1 #相当于i_num_count = i_num_count + 1
    else: #输入的不是数字
        print('非法输入，必须输入一个整数数字！')

print(list_input)

        
    
        

