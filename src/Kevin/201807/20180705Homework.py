'''
作业: 关于列表的一些计算
1. 写一个函数calc_list_maxvalue(x), 传入一个全是数字的list x，函数用来计算这个list中最大的数字，打印结果并返回
2. 写一个函数calc_list_minvalue(x), 传入一个全是数字的list x，函数用来计算这个list中最小的数字，打印结果并返回
3. 写一个函数calc_list_summary(x), 传入一个全是数字的list x，函数用来计算这个list中所有数字的和，打印结果并返回
4. 写一个函数calc_list_average(x), 一个全是数字的list x，函数用来计算这个list中所有数字的平均值，打印结果并返回
5. 写一个函数calc_list_hasvalue(x, element),传入 传入一个全是数字的list x，以及另外一个数字element，
        函数用来判断element在list x中出现的次数，打印结果并返回
6. 写一个函数add_value_to_list(x, element), 传入一个全是数字的list x，以及另外一个数字element，
        如果element在list x中不存在，则把它加进去，否则不添加, 打印整个列表的元素并返回
7. 写一个函数remove_duplicate_from_list(x), 传入一个全是数字的list x，
        用来删除列表中重复的元素，删除之后列表中所有元素都不重复, 打印删除前以及删除后的列表并返回
        例如列表中以前有[1,2,3,1,2,3]6个元素，调用函数之后，列表中应该只剩下[1,2,3]三个元素        

-----------高级------------------
8. 写一个函数sort_list(x), 传入一个列表x, 将列表中的元素按从小到大的顺序排列，打印排好序的列表并返回


'''

'''
1. 写一个函数calc_list_maxvalue(x), 传入一个全是数字的list x，函数用来计算这个list中最大的数字，打印结果并返回
'''

def calc_list_maxvalue(x):
    j = x[0]
    for i in range(len(x)):
        if j < x[i]:
            j = x[i]
    print(f'List{x}中最大的元素是：{j}')
    return j
calc_list_maxvalue(x = [1, 2, 3, 9, 0, 6, 8, 4, 5])

'2. 传入一个全是数字的list x，函数用来计算这个list中最小的数字，打印结果并返回'

def calc_list_minvalue(x):
    j = x[0]
    for i in range(len(x)):
        if j > x[i]:
            j = x[i]
    print(f'List{x}中最小的元素是：{j}')
    return j
calc_list_minvalue(x = [1, 2, 3, 9, 0, 6, 8, 4, 5])
'3. 写一个函数calc_list_summary(x), 传入一个全是数字的list x，函数用来计算这个list中所有数字的和，打印结果并返回'
def calc_list_summary(x):
    p = 0
    for i in x:
        p += i 
    
    print(f'List{x}这写些数的和是：{p}')
    return p
calc_list_summary(x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

t = [5, 6, 8, 9, 7, 5, 8, 4]

'4. 写一个函数calc_list_average(x), 一个全是数字的list x，函数用来计算这个list中所有数字的平均值，打印结果并返回'

def calc_list_average(e):
    fj = calc_list_summary(x = e)
    k = fj / len(e)
    print(f'List{e}这写些数的平均数是：{k}')
    return k
print(calc_list_average(e = t))

'''5. 写一个函数calc_list_hasvalue(x, element),传入 传入一个全是数字的list x，以及另外一个数字element，
                函数用来判断element在list x中出现的次数，打印结果并返回'''

def calc_list_hasvalue(x, element):
    f = x.count(element)
    print(f'List{x}element在x中出现次数是：{f}')
    return f
result = calc_list_hasvalue(x = t, element = 4)
print(result)

'''6. 写一个函数add_value_to_list(x, element), 传入一个全是数字的list x，以及另外一个数字element，
                如果element在list x中不存在，则把它加进去，否则不添加, 打印整个列表的元素并返回'''

def add_value_to_list(x, element):
    result = calc_list_hasvalue(x = x, element = element)
    if result == 0:
        x.append(element)

    print(x)
s = []
add_value_to_list(x = s, element = 2)
add_value_to_list(x = s, element = 2)
add_value_to_list(x = s, element = 4)
add_value_to_list(x = s, element = 4)
add_value_to_list(x = s, element = 4)



def remove_duplicate_from_list(x):
    g = [1, 2, 2, 2]
    temp = []
    for ele in x:
        add_value_to_list(x = temp, element = ele)
    x = temp
    return temp

lst = [1,2,3,1,2,3,4]
lst = remove_duplicate_from_list(x = lst)
print(lst)
        