import turtle
pen = turtle.Turtle()
def drawA(p):
    p.fd(100)
    p.lt(120)
    p.bk(100)
    p.fd(200)
    p.rt(240)
    p.fd(200)

#drawA(p = pen)

def drawA2(p, m):
    p.fd(100 * m)
    p.lt(120)
    p.bk(100 * m)
    p.fd(200 * m)
    p.rt(240)
    p.fd(200 * m)
    p.rt(240)


for i in range(5):
    drawA2(p = pen, m = i + 1)




turtle.mainloop()