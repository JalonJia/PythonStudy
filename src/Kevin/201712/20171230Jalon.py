import turtle
pen = turtle.Turtle()


def dbx(p, n, x):
    for i in range(x):
        p.fd(n)
        p.lt(360/x)

def dbx_color(p, n, x, r, g, b):
    pen.color(r, g, b)
    pen.begin_fill()
    dbx(p, n, x)
    pen.end_fill()


#设置颜色，每个参数不能超过1
pen.color(0.1, 0.5, 0.1) #同时设置线以及填充的颜色
pen.pencolor(0, 0, 0) #只设置线的颜色
pen.fillcolor(0.5, 1, 1) #只设置填充的颜色
#开始涂色
pen.begin_fill()

dbx(pen, 100, 3)

#结束涂色
pen.end_fill()

dbx_color(pen, 100, 6, 0.1, 1, 1)
dbx_color(pen, 120, 8, 0.3, 0.1, 1)

turtle.mainloop() 