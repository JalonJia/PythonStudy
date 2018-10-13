#递归 - 科赫曲线

import turtle

def koch_kurve(pen, len_x):
    if len_x <= 3:
        pen.fd(len_x)
        return
    
    koch_kurve(pen, len_x/3)
    pen.lt(60)
    koch_kurve(pen, len_x/3)
    pen.rt(120)
    koch_kurve(pen, len_x/3)
    pen.lt(60)
    koch_kurve(pen, len_x/3)


if __name__ == '__main__'   :
    pen = turtle.Turtle()
    pen._delay(0.01)
    koch_kurve(pen, 1000)
    turtle.mainloop()
     
    
