import math

#三个函数
i = int('3')
print(i)

i = int('8')
print(i)

f = float('3.5559999')
print(f)

f = float('2898.2')
print(f)

s = str(f)
print(s)

s = str(i)
print(s)

print(type(i))
print(type(f))
print(type(s))

#定义函数
def xAdd(a, b, c):
    d = a + b
    d = d + c
    return d

    
x = xAdd(1, 2, 3)
print(x)

x = xAdd(3, 34, 1)
print(x)

s = xAdd('我', 'Kevin', '爱学习')
print(s)

s = 'a'
print(' ' * (50-len(s)) + s)

s = 'abc'
print(' ' * (50-len(s)) + s)

s = 'akjsdfkasjdfaksdfiqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqdw'
print(' ' * (50-len(s)) + s)

print('+', '-', '|', end=' ')
print('+', '-', '|', end=' ')

'''
+------+-----+
|            |
|            |
|            |
|            |
|            |
'''


