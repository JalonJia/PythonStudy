'''
Created on 2018年5月26日

@TOOD: 摞方块
@author: jalon
'''

import turtle

pen = turtle.Turtle()

pen.setx(0) #设置X坐标
pen.sety(0) #设置Y坐标
pen.setpos(0, 0) #将光标设置到指定位置 
pen.seth(0) #改变画图方向,向右画 .向上是seth(90),向左seth(180),向下(270)

def draw_polygon(pen, side_len, side_cnt):
    pen.seth(0)
    for i in range(side_cnt):
        pen.fd(side_len)
        pen.lt(360/side_cnt)

'''
摞多边形
pen: 画笔
level_cnt: 层数
'''
def accumulate_polygon(pen, level_cnt):
    side_len = 100
    gap_len = 20
    side_cnt = 4
    x = 0
    y = 0
    
    for level in range(level_cnt):
        for col in range (level + 1):
            pen.pu()
            pen.setpos(x, y)
            pen.pd()
            draw_polygon(pen, side_len, side_cnt)
            x += (side_len + gap_len)
        
        x = 0    
        y += (side_len + gap_len)
        
def accumulate_polygon2(pen, level_cnt):
    side_len = 100
    gap_len = 20
    side_cnt = 3    
    x = 0
    y = 0
    
    for level in range(level_cnt):
        for col in range (level + 1):
            pen.pu()
            pen.setpos(x, y)
            pen.pd()
            draw_polygon(pen, side_len, side_cnt)
            x += (side_len + gap_len)
        
        row_width = (side_len + gap_len) * (level + 1) - gap_len
        x = -int(row_width / 2)   
        y -= (side_len + gap_len)
        


accumulate_polygon2(pen, 5)

turtle.mainloop()

    
    
    