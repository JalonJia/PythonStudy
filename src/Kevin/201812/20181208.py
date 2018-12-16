import turtle
class Point:
    pass

class Rectangle:
    pass


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

def draw_rect(p, rect):
    draw_the_rectangle(pen, rect.corner.x, rect.corner.y, rect.width , rect.height)
    

if __name__ == '__main__':
    pen = turtle.Turtle()
    vi = Rectangle()
    vi.corner = Point()
    vi.corner.x = 300.0
    vi.corner.y = 400.0 
    vi.width = 200
    vi.height = 100
    
    draw_rect(pen, vi)

    turtle.mainloop()
