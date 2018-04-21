import turtle
import math
pen = turtle.Turtle()

pen._delay(0.01)

def n_bianxing_part(p, n, l, part):
    for i in range(part):
        p.fd(l)
        p.lt(360/n)

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

def draw_D(p, f):  
    r0 = 100
    yuanhu_dushu(p = pen, r = r0 * f, degree = 180)
    p.lt(90)
    p.fd(2 * r0 * f * 2)
    p.lt(90)


'''
draw_D(p = pen, f = 2)
draw_D(p = pen, f = 3)
'''

def draw_B(p, f):  
    r0 = 50
    yuanhu_dushu(p = pen, r = r0 * f, degree = 180)
    p.rt(180)
    yuanhu_dushu(p = pen, r = r0 * f, degree = 180)    
    p.lt(90)
    p.fd(2 * r0 * f * 2)
    p.lt(90)    
    p.fd(1)

'''draw_B(p = pen, f = 2)
draw_B(p = pen, f = 3)'''

f = [3, 9, 2, 7]

def min_list(j, k):
    for i in range(3):
        if j < k[i]:
            j = k[i]
    print(j)

min_list(j = f[0], k = f)


turtle.mainloop()