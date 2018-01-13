import turtle
pen = turtle.Turtle()
print(pen)




#pen.pu()
#pen.fd(9)
#pen.rt(90)
#pen.pd()    
#for iLoop in range (5):
#    pen.fd(10)
#    pen.rt(90)


def drawTa(x):
    pen.clear()
    n = 5
    for iLoop in range (x):
        pen.fd(n) 
        pen.rt(90)
        pen.fd(n)  
        pen.rt(90)
        n = n + 5
    


def add(a, b):
    return a+b+b+a

print(add(10,20))


drawTa(20)














turtle.mainloop()