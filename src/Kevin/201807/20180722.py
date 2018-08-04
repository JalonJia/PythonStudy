j = int(input('请输入0到几的乘法表'))
y = 1
t = 1

while y <= j:
    h = 0
    for i in range(y):
        h += 1
        u = t * h
        print(f'{h} * {t} = {u} ', end = '')
    print()
    t += 1
    
    y += 1