import turtle
pen1 = turtle.Turtle()

def sanjiao(h, pen):
    for t in range(3):
        pen.fd(h)
        pen.lt(360/3)


sanjiao(200, pen1)
sanjiao(h = 300, pen = pen1)

pen1.reset()

def sanjiao_color(pen, l, r, g, b):
    pen.color(r, g, b)
    pen.begin_fill()
    sanjiao(l, pen)
    pen1.end_fill()

sanjiao_color(pen = pen1, l = 50, r = 1, g = 0, b = 0) 
sanjiao_color(pen = pen1, l = 60, r = 0, g = 0, b = 1)
#pen1.color(0, 1, 0)
#pen1.begin_fill()

#sanjiao(100, pen1)

#pen1.end_fill()


turtle.mainloop()
