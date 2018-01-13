import turtle
pen = turtle.Turtle()
#print(pen)


def drawTa(x):
    pen.reset() #reset会把屏幕清空，同时乌龟回到原位
    n = 5
    for iLoop in range (x):
        pen.fd(n) 
        pen.rt(90)
        pen.fd(n)  
        pen.rt(90)
        n = n + 5
    return None

#定义函数，并返回
def add(a, b):
    return a+b

c = add(add(add(10, 20), 30), 40)
print(c)


#drawTa(10)
#drawTa(4)

#For循环嵌套
'''
s1 = '%s乘  %s = %s'
for i in range(9):
    a = i+1
    for iLoop in range (a):
        print(s1 % (iLoop + 1, a, (iLoop + 1) * a))

'''

#while循环
s2 = '%s乘  %s = %s'
n = 1
while n <= 9:
    print(n)
    print(s2 % (n, 9, 9*n))
    n = n + 1

print('==================For 循环=====================')
#跟上面一样的含义
n = 1  
for n in range(1, 10):
    print(n)
    print(s2 % (n, 9, 9*n))
    
    

print(n)
print("After While!!!!!!")


print(list(range(1, 11)))







turtle.mainloop()