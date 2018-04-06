import turtle
import math
pen = turtle.Turtle()


def nbianxing(p, n, l):
    for i in range(n):
        p.fd(l)
        p.lt(360/n)

def yuanxing(p, r):
    h = math.pi * r * 2
    n = math.floor(h/3)

    nbianxing(n= n, p=p, l=3)
    
yuanxing(p = pen, r = 100)

turtle.mainoop()