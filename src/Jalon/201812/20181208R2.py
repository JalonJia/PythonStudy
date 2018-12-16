import turtle

class Point:
    """
    坐标
    属性：x，y
    """
    
class Rectangle:
    """
            矩形
    属性：左下角的坐标，宽度，高度
    """
    
box = Rectangle()
box.corner = Point()
box.corner.x = 100.0
box.corner.y = 200.0
box.width = 120.0
box.height = 200.0

def draw_rect(pen, rect):
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



    
pen2 = turtle.Turtle()
draw_rect(pen2, box)
    

turtle.mainloop()


