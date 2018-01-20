#��/usr/bin/python
#-*- coding: utf-8 -*-

import turtle

pen = turtle.Turtle()

#正方形
for i in range(1):
    pen.fd(100)
    pen.lt(90)

pen.reset() #清除面板

#平行线
pen.fd(100)
pen.up()
pen.lt(90)
pen.fd(50)
pen.lt(90)
pen.down()
pen.fd(100)

pen.reset()

#定义函数-画多边形
def drawRect(pen, edgeCnt):
    for i in range(edgeCnt):
        pen.fd(100)
        pen.lt(360/edgeCnt)


drawRect(pen, 5)
drawRect(pen, 10)




turtle.mainloop()