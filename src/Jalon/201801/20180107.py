import turtle
import math


pen = turtle.Turtle()
pen._delay(0.01)

#多边形的一部分
"""
dPart: 0-1之间的数字，代表百分比
"""
def drawPartRect(pen, edgeCnt, iLen, dPart):
    iCnt = math.floor(edgeCnt * dPart)
    for i in range(iCnt):
        pen.fd(iLen)
        pen.lt(360/edgeCnt)

def drawPartRectColor(pen, edgeCnt, iLen, dPart, red, green, blue):
    pen.fillcolor(red, green, blue)
    pen.pencolor(red, green, blue)
    pen.begin_fill()
    drawPartRect(pen, edgeCnt, iLen, dPart)
    pen.end_fill()

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


def move_to(pen, x, y):
    pen.pu()
    pen.setpos(x, y)
    pen.seth(0)
    pen.pd()
    
"""
指定位置画横线
"""
def drawLine(pen, x, y, iLen):
    move_to(pen, x, y)
    pen.fd(iLen)  
    

def drawPartCircle(pen, r, dPart):
    lLen = math.pi * 2 * r
    n = math.floor(lLen / 3)
    drawPartRect(pen, n, 3, dPart)

def drawPartCircleColor(pen, r, dPart, red, green, blue):
    lLen = math.pi * 2 * r
    n = math.floor(lLen / 3)
    drawPartRectColor(pen, n, 3, dPart, red, green, blue)


pen.setpos(0, 0)
pen.seth(0) #设置方向向右
drawPartCircleColor(pen, 100, 1, 1, 0, 0)
pen.seth(180) #设置方向向右
drawPartCircleColor(pen, 150, 1, 0, 1, 0)
pen.pencolor(0, 0, 1)
drawLine(pen, -40, 130, 20)
drawLine(pen, 20, 130, 20)
move_to(pen, -35, 100)
drawPartRectColor(pen, 8, 10, 1, 0, 0, 0)
move_to(pen, 25, 100)
drawPartRectColor(pen, 8, 10, 1, 0, 0, 0)

move_to(pen, -10, 70)
drawPartRectColor(pen, 3, 20, 1, 0, 0, 0)


move_to(pen, 200, 200)




turtle.mainloop()