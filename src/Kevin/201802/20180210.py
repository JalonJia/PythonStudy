def lianjia(l, n):
    for d in range(1, n + 1):
       l = l + d
       print(l)
    
lianjia(l = 0, n = 100)

import turtle       
pen = turtle.Turtle()
    
def zhengfangxing(c):
    for i in range(4): 
        pen.fd(c)
        pen.lt(90)    
    
zhengfangxing(c = 100)
zhengfangxing(c = 200)