import turtle
pen = turtle.Turtle()


def clr(v): 
    for h in range(3):
        v.color(1,0,0)
        v.begin_fill()#开始涂色
        v.fd(90)
        v.lt(360/3)       
        v.end_fill()#结束涂色
        
clr(pen)

turtle.mainloop()