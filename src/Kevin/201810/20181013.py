import turtle
pen = turtle.Turtle()
pen._delay(0.01)
pen.pu()
pen.lt(180)
pen.fd(700)
pen.rt(180)
pen.pd()
def Koch_Curve (jkl):
    if jkl <= 3:
        pen.fd(jkl)
        return
    Koch_Curve(jkl/3)
    pen.lt(60)
    Koch_Curve(jkl/3)
    pen.rt(120)
    Koch_Curve(jkl/3)
    pen.lt(60)        
    Koch_Curve(jkl/3)
Koch_Curve (800000000000)
turtle.mainloop()