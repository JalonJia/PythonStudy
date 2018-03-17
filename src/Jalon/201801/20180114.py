
list_a = [999, 100, 2, 3, 4] #一个列表，包含了5个元素
list_s = ['Kevin', 'Miya', 'Nani', 'Jalon']  #一个列表，包含了4个元素

print(list_a)
print(list_s)

#求列表的和
total = 0
for i in list_a: #循环的时候，会依次获取下一个元素，一直到最后一个元素
    print(i)
    total = total + i

print(total)


for s in list_s: #循环的时候，会依次获取下一个元素，一直到最后一个元素
    print(s)

for i in range(len(list_s)):
    print(list_s[i])
        


print('第4个元素的值：%s' % list_a[3])

#往列表最后追加元素
list_a.append(5)
list_a.append(6)
list_a.append(7)
list_a.append(8)
list_a.append(9)
list_a.append(1000)

list_a[4] = 100
list_a[5] = 600

print(list_a)

print('数组%s的长度是：%s' % ('list_a', len(list_a)))
if len(list_a) >= 10:
    print('第10个元素的值：%s' % list_a[9])


#列表可以相加
list_c = list_a + list_s
print(list_c)

#列表可以乘以一个数组进行重复
print(list_c * 2)

#list不支持减法
#list_d = list_c - list_s

s_1 = 'ABC'
s_2 = 'C'
#s_3= s_1 - s_2 #字符串也不支持相减



#获取列表的一部分
print(list_a[2 : 4])
print(list_a[2 : ]) #从下标2到最后一个
print(list_a[ : 4]) #从下标0到第4个
print(list_a[ : ])

print(list_a[-1]) #倒数第一个元素
print(list_a[-2])
print(list_a[-5 : -2])
 
#冒泡排序法
def sort_list(listx):
    for i in range(len(listx)):
        e = listx[i]
        for j in range(i, len(listx)):
            #print(e)
            #print(listx)
            if e > listx[j]:
                listx[i] = listx[j]
                listx[j] = e
                e = listx[i]
    return listx


print(sort_list(list_a))
print(sort_list(list_s))
#print(sort_list(list_c)) #数字，字符串不能比较大小