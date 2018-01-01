#./usr/bin/python
#-*- coding: utf-8 -*-

import turtle
import math

pen = turtle.Turtle()
pen._delay(0.01)


#定义函数-画多边形
def drawRect(pen, edgeCnt, iLen):
    for i in range(edgeCnt):
        pen.fd(iLen)
        pen.lt(360/edgeCnt)

def drawCircle(pen, r):
    lLen = math.pi * 2 * r
    n = math.floor(lLen / 3)
    drawRect(pen, n, 3)
    


drawCircle(pen, 100)
drawCircle(pen, 200)










turtle.mainloop()