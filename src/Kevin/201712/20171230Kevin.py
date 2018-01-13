import turtle
pen = turtle.Turtle()
print(pen)

def print_lyrics():
    print("I'm a lumberjecK, and I'm oKay")
    print("I sleep all night I worK all day.")
    
print_lyrics()
m = 97
def sjx(p, n):
    p.fd(n)
    p.lt(360/3)  
    p.fd(n)
    p.lt(360/3)
    p.fd(n)
    p.lt(360/3)

m = 100  
sjx(pen, m)

m = 200
sjx(pen, m)

m = 300
sjx(pen, m)

sjx(pen, 50)

turtle.mainloop()    