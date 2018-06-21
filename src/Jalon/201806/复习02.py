'''
复习以前的内�?
列表

'''
from test.test_binop import isnum

# 列表
# 空列�?
list_a = []
# 添加元素
list_a.append(1)
list_a.append(2)
# insert向指定的位置的前面插入新的元�?
list_a.insert(0, 0)

print(list_a)

# x = list_a[1] #下标�?0�?�?
'''
#pop可以从列表中拿走指定位置的元素，不写参数代表拿走�?后的元素
x = list_a.pop()
print(x)
print(list_a)
x = list_a.pop(1)
print(x)
x = list_a.pop()
print(x)
x = list_a.pop(-2)
print(x)
'''

# 列表可以+�? *
list_b = list_a * 3
list_c = list_a + list_b
print(list_c)

list_d = ['a', 'b', 'c']
list_c.insert(3, list_d)
print(list_c)

l = len(list_c)
print(l)

for x in list_c:
    if isnum(x):
        x += 100
    print(x)
    
print(list_c)    

for x in range(len(list_c)):
    if isnum(list_c[x]):
        list_c[x] += 100
    print(list_c[x])

print(list_c)
    
# for x in range(len(list_c)):
#    if isnum(list_c[x]):
#        list_c.remove(list_c[x])
    # print(list_c[x])

list_c.append(100)
print(list_c)
# count可以计算�?个元素在列表中出现的次数 
l = list_c.count(101)
print(l)

# 反转列表
list_c.reverse()
print(list_c)

# 查找�?个元素的下标
x = list_c.index(101)
print('101的下标：%s' % x)

x = list_c.index(101, 3)
print('101的下标：%s' % x)

'''
id_x = 0
while id_x != -1
for x in list_c:
    if x == 101:
        print
'''

# 删除�?个元素，括号里传入元素的值，如果有多个传入的值，只会删除第一�?
list_c.remove(100)
print(list_c)    

list_c.insert(6, 99)
list_c.insert(8, 999)
print(list_c)    

for x in list_c:
    if x == 99:
        continue
    elif x == 999:
        break
    else:
        print(x)
    
    print("-" * 60)

