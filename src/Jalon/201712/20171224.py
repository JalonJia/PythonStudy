#./usr/bin/python
#-*- coding: utf-8 -*-

import turtle
import math

pen = turtle.Turtle()
pen._delay(0.01)

#矩形
def drawRect(pen, iWhith, iHeight):
        pen.fd(iWhith)
        pen.lt(90)
        pen.fd(iHeight)
        pen.lt(90)
        pen.fd(iWhith)
        pen.lt(90)
        pen.fd(iHeight)
        pen.lt(90)

#半个多边形
def drawHalfRect2(pen, edgeCnt, iLen):
    for i in range(int(edgeCnt/2)):
        pen.fd(iLen)
        pen.lt(360/edgeCnt)
        
def drawHalfCircle(pen, r):
    lLen = 2 * math.pi * r
    n = math.floor(lLen / 3)
    drawHalfRect2(pen, n, 3)
    
#多边形
def drawRect2(pen, edgeCnt, iLen):
    for i in range(edgeCnt):
        pen.fd(iLen)
        pen.lt(360/edgeCnt)

    
def drawCircle(pen, r):
    lLen = math.pi * 2 * r
    n = math.floor(lLen / 3)
    drawRect2(pen, n, 3)
    

pen.setpos(0, 0)
pen.begin_fill()
drawHalfCircle(pen, 100)
pen.end_fill()

pen.begin_fill()
pen.fillcolor(1,1,1)
#pen.color(1, 1, 1)
drawHalfCircle(pen, 100)
pen.end_fill()




pen.setpos(0, 0)
pen.seth(180) #设置方向向左
pen.fillcolor(0.2,0.6,0.7)
pen.pencolor(0.6, 0.8, 0.5)
pen.begin_fill()
drawCircle(pen, 200)
pen.end_fill()










turtle.mainloop()