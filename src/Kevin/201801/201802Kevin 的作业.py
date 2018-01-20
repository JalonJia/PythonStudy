import turtle
pen = turtle.Turtle()


def yh(g):   
    y = 1
    for r in range(g):
        y = y * (r + 1) 
        print(y)
    return y

yh(10)

#def ER(K):
    #y = 1 
    #for r in range(y): 
        #y = (10+y)        
        #K.fd(y)
        #K.lt(90)
        #return y
                                        
#ER(24)

print(' ' * 69 + "a")
print(' ' * 68 + "ab")
print(' ' * 67 + "abc")
w = 'abcd'
print(' ' * 66 + w)
r = 70 - len(w)
print(r)
print(' ' * r + w)  
w = 'I Im Kevin'
r = 70 - len(w)
print(' ' * r + w)

def print70(e):
    l = 70 - len(e)
    print(' ' * l + e)

print70("j")    
print70("fgg")
print70("jbzbghx")
print70("jgbbx")
print70("jbfghs")

y = 100
pen.fd(y)
pen.lt(360/3)
pen.fd(y)
pen.lt(360/3)
pen.fd(y)
pen.lt(360/3)
def qj(t, e):
    for g in range(3):
        e.fd(t)
        e.lt(360/3)

qj(253, pen)
qj(678, pen)


turtle.mainoop()