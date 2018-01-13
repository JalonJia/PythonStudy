import turtle
pen = turtle.Turtle()


def clr(v): 
    for h in range(3):
        v.begin_fill()  
        v.color(0.1, 0.5, 0.1)
        v.fd(90)
        v.lt(360/3)       
        v.end_fill()    
        
clr(pen)

turtle.mainloop()