import turtle
import math

bob = turtle.Turtle()
print(bob)

bob.speed(0)

#画圆
r = 10 #圆的半径
#周长=2*pi*半径
'''
zhouchang = 2 * math.pi * r
bob.pu()
bob.fd(r)
bob.rt(90)
bob.pd()

for i in range (10):    
    bob.fd(zhouchang/10)
    bob.rt(360/10)
    
bob.rt(360/10)
bob.lt(90)
bob.bk(r)
'''    
    

#第二步：抽象成函数
def drawCircle(pen, ra): #两个参数， 画图工具、半径
    zc = 2 * math.pi * ra #计算周长
    bc = 3
    n = math.ceil(zc/bc) #边长
    pen.pu()
    pen.fd(ra)
    pen.rt(90)
    pen.pd()    
    for iLoop in range (n):
        pen.fd(zc/n)
        pen.rt(360/n)
    
    pen.pu()
    pen.lt(90)
    pen.bk(ra)
    pen.pd()
    

drawCircle(bob, 10)
drawCircle(bob, 100)
drawCircle(bob, 200)
drawCircle(bob, 300)


turtle.mainloop()



