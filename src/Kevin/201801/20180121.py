import turtle
import math #数学模块

bob = turtle.Turtle()
turtle.delay(0.01) #加快绘画速度


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(t = bob, length = 100)
square(t = bob, length = 200)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(t = bob, length = 100, n = 10)
polygon(t = bob, length = 10, n = 150)
def circle(t, length, n, r):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
        
#提示：圆的周长=圆的半径r*2*math.pi
#例如：半径100的圆，周长=2*math.pi*100
r = 100
zhouchang = math.pi * 2 * r
print(zhouchang)
#可以用一个多边形画出一个近似的圆，每条边长3个像素
#math.floor(f)函数可以获得一个小数的整数部分，比如1.2的整数部分是1
polygon(t = bob, length = 3, n = math.floor(zhouchang/3))




turtle.mainloop()