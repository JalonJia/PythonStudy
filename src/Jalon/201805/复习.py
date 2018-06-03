'''
复习以前的内容


'''

#变量
a = 100
print(a)

jiajikai = '贾继开'
print(jiajikai)

#运算符
a = 100
b = 2
c = a + b
c = a - b
c = a * b
c = a / b
c = a % b
print(c)
c = a ** b #乘方
print(c)

#字符串
jiajikai = '贾继开'
jiamm = '贾淼淼'
#字符串操作
s = jiajikai + jiamm
print(s)
#s = s - jiamm 字符串没有减法
#print(s)
s = s * 10
print(s)
#切片
s02 = s[2]
print(s02)
s_left5 = s[0: 5] #取前五个字符
print(s_left5)
s_left5 = s[: 5]
print(s_left5)
s_mid = s[10: 20]
print(s_mid)
s_right5 = s[-5: ]
print(s_right5)
s_all = s[ : ]
print(s_all)
s_rev = s[ : : -1] #如果有第三个参数, 第三个参数是步长   
print(s_rev)
s_jump = s[0:10:2]
print(s_jump)
#字符串最后一个字符
print(s[len(s) - 1])
print(s[-1])

#打印每个字符
#for c in s:
#    print(c)
#for i in range(len(s)):
#    print(s[i])
s_base = 'My name is: %s, I am %d years old.'
s_jiajikai = s_base % (jiajikai, 9)
print(s_jiajikai)


#列表


#for循环
for i in range(100):
    pass

    #print(i)

#while循环

#if else
#break
#continue
#return

#函数





