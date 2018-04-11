import turtle
import math
from math import degrees
pen = turtle.Turtle()

'''
l：边长
p：画笔
n：多边形的边数
part: 多边形的一部分，需要传要画出来的边数
'''
def n_bianxing_part(p, n, l, part):
    for i in range(part):
        p.fd(l)
        p.lt(360/n)

#n_bianxing_part(p = pen, n = 4, l=100, part = 2)
#n_bianxing_part(p = pen, n = 100, l=2, part = 25)

'''
p：画笔
r: 半径
degree: 圆弧的度数
'''
def yuanhu_dushu(p, r, degree):
    zhouchang = 2 * math.pi * r
    bianshu = math.floor(zhouchang / 3) #画3个像素的多边形模拟圆形 #math.floor求商
    part = math.floor(bianshu * degree / 360)  #要画的弧度包含的边数，即要画的多边形的边数
    n_bianxing_part(p = p, n = bianshu, l = 3, part = part)

#yuanhu_dushu(p = pen, r = 100, degree = 180)
#yuanhu_dushu(p = pen, r = 200, degree = 360)


'''
p：画笔
r: 半径
degree: 圆弧的度数
'''
def n_yuanhu_dushu(p, r, degree, n):
    for i in range(n):
        yuanhu_dushu(p = p, r = r, degree = degree)
        p.lt(360/8)

n_yuanhu_dushu(p = pen, r = 100, degree = 180, n = 3)



turtle.mainloop()