import turtle
pen2 = turtle.Turtle()
print(pen2)

m = 200

def zfx(pen, n, x):
    for i in range(x):
        pen.fd(n)
        pen.lt(360/x)

zfx(pen2, 100, 5)

zfx(pen2, 150, 8)
zfx(pen2, 200, 6)

turtle.mainloop()    