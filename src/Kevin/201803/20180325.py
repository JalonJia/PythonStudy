import turtle
import math
pen = turtle.Turtle()

'''for i in range(3):
    pen.fd(100)
    pen.lt(360/3)

for i in range(4):
    pen.fd(100)
    pen.lt(90)'''

def nbianxing(n, p, l):    
    for i in range(n):
        p.fd(l)
        p.lt(360/n)

#nbianxing(n = 614, p = pen, l = 3)

def yuanxing(p, r):
    h = math.pi * r * 2 #周长
    n = math.floor(h / 3) #边数=周长/每段线段的长度（这里是3个像素）。因为有可能没有整除，所以需要用math.floor函数获取这个小数的整数部分
    nbianxing(n= n, p=p, l=3)
    
yuanxing(p = pen, r = 100)

turtle.mainloop()