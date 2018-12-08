import turtle
pen = turtle.Turtle()
class Point:
    pass
class Rectangle:
    pass
vi = Rectangle()
vi.corner = Point()
vi.corner.x = 300.0
vi.corner.y = 400.0 
vi.width = 200
vi.height = 100
def draw_the_rectangle(p, j, k, l, m):
    p.pu()
    p.rt(90)
    p.fd(j)
    p.rt(90)
    p.fd(k)
    p.pd()
    p.fd(l)
    p.rt(90)
    p.fd(m)
    p.rt(90)
    p.fd(l)
    p.rt(90)
    p.fd(m)
    p.rt(90)
    
draw_the_rectangle(pen, vi.corner.x, vi.corner.y, vi.width , vi.height)
