import turtle
pen = turtle.Turtle()

list_input = []
s_input = ''
j = 0

def draw_square(p, ):






while j < 4:
    s_input = input("请输入一个数字:")
    if s_input.isdigit():
        j += 1
        list_input.append(int(s_input))
    else:
        print("非法输入，请输入一个数字。")

print(list_input)

def square(r, t, u, j):
    if ((r == t) and (u == j)) or ((r == j) and (u == t)) or ((r == u) and (t == j)):
        print('能组成正方形')
    else:
        print('对不起，这四个长度不能组成长方形')
        
'''   
    if (r == j) and (u == t):
        print('能组成正方形')
    else:
    
    if (r == u) and (t == j):
        print('能组成正方形')
    else:

    
    if t == u:
        print('能组成正方形')
'''

square(r = list_input[0], t = list_input[1], u = list_input[2], j = list_input[3])

turtle.mainoop()