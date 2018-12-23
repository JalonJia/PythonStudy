import math
import turtle

class Point:
    """
    x
    y
    """
    
class Circle:
    """
    center ： 、Point对象
    radius
    """

class Rectangle:
    """
            矩形
    属性：左下角的坐标，宽度，高度
    corner：Point对象
    width：int
    height：int
    """


def point_in_Circle(p, circle):
    """
    p:Point对象
    circle：Circle对象
    """
    a = p.x-circle.center.x
    b = p.y - circle.center.y
    c = math.sqrt(a**2 + b**2)
    if c <= circle.radius:
        return True
    else :
        return False
    
    

def draw_circle(r, f):
    r.seth(0) #光标向右
    r.setpos(0, 0)
    r.lt(90)
    r.pu()
    r.fd(f.center.y)
    r.rt(90)
    r.fd(f.center.x)
    r.fd(f.radius)
    r.lt(90)
    r.pd()
    z = 2*math.pi*f.radius
    w = int(z/2)
    for i in range(w):
        r.fd(2)
        r.lt(360/w)
            
            
def draw_rect(pen, rect):
    pen.seth(0) #光标向右
    pen.setpos(0, 0)
    pen.pu()
    pen.fd(rect.corner.x)
    pen.lt(90)
    pen.fd(rect.corner.y)
    pen.rt(90)
    pen.pd()
    pen.fd(rect.width)
    pen.lt(90)
    pen.fd(rect.height)
    pen.lt(90)
    pen.fd(rect.width)
    pen.lt(90)
    pen.fd(rect.height)




def draw_point(r, f):
    g = f.x-1
    r.pu()
    r.setpos(0, 0)
    r.seth(0)
    r.lt(90)
    r.fd(f.y)
    r.rt(90)
    r.fd(g)
    r.pd()
    r.fd(1)
    r.pu()
    r.setpos(0, 0)
    r.pd()


def rectangle_in_the_circle(circle, rect):
    """
    rect:Rectangle对象
    circle：Circle对象
    TODO：函数用来判断矩形rect是否落在圆circle里面
    返回值：如果在里面返回True，否则返回False
    算法：判断矩形4个角的坐标是不是都落在圆里面
    """
        
    #判断左下角的坐标点
    b_in_circle = point_in_Circle(rect.corner, circle)
    if not b_in_circle:
        return False
    
    #判断右下角的坐标点
    point = Point()
    point.x = rect.corner.x + rect.width
    point.y = rect.corner.y
    b_in_circle = point_in_Circle(point, circle)
    if not b_in_circle:
        return False
    
    #判断左上角的坐标点
    point.x = rect.corner.x 
    point.y = rect.corner.y + rect.height
    b_in_circle = point_in_Circle(point, circle)
    if not b_in_circle:
        return False
    

    #判断右上角的坐标点
    point.x = rect.corner.x + rect.width
    point.y = rect.corner.y + rect.height
    b_in_circle = point_in_Circle(point, circle)
    if not b_in_circle:
        return False
    
    #四个顶点都在圆里面
    return True
    
    
#实例化对象
j = Circle()
j.center = Point()
j.radius = 75
j.center.x = 150
j.center.y = 100

p = Point()
p.x = 160
p.y = 140

h = point_in_Circle(p, j)
print(h)

pen = turtle.Turtle()
pen._delay(0.01)

draw_circle(pen, j)
draw_point(pen, p)

box = Rectangle()
box.corner = Point()
box.corner.x = 110
box.corner.y = 70
box.width = 100
box.height = 50
draw_rect(pen, box)

print(rectangle_in_the_circle(j, box))


turtle.mainloop()