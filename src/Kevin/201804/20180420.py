import turtle


def draw_square(p, f, j):
    if j > f:
        p.lt(90)
    p.fd(f)
    p.lt(90)
    p.fd(j)
    p.lt(90)    
    p.fd(f)
    p.lt(90)
    p.fd(j)


def square(pen, r, t, u, j):
    if ((r == t) and (u == j)):
        print('能组成长方形')
        draw_square(p = pen, f = list_input[1], j = list_input[3])        
    elif ((r == j) and (u == t)):     
        print('能组成长方形')
        draw_square(p = pen, f = list_input[1], j = list_input[3])        
    elif ((r == u) and (j == t)):         
        print('能组成长方形')
        draw_square(p = pen, f = r, j = j)
    else:
        print('对不起，这四个长度不能组成长方形')
        

    
list_input = []
s_input = ''
j = 0

while j < 4:
    s_input = input("请输入一个数字:")
    if s_input.isdigit():
        j += 1
        list_input.append(int(s_input))
    else:
        print("非法输入，请输入一个数字。")

print(list_input)

pen = turtle.Turtle()
square(pen = pen, r = list_input[0], t = list_input[1], u = list_input[2], j = list_input[3])

turtle.mainloop()