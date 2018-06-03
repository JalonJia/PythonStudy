'''
TODO: 2018-5-20周作业
画一个摞箱子的程序，指定要摞几层箱子，画出箱子的摆放图形,类似下面的图像；
口
口 口
口 口 口
口 口 口 口
'''
import turtle
pen = turtle.Turtle()
print(pen)

j = 1
k = 1

while k == 11:
    for i in range(1):
        pen.fd(1000 ( * k))
        pen.pu()
        pen.rt(90)
        pen.fd(1000)
        pen.lt(180)
        pen.pd()
    k = k + 1   
    
turtle.mainloop()                