#函数1：Hello+Name
def HelloName(Name):
    #print('Hello ' + Name)
    print('Hello %s' % Name)

#HelloName('JiaJikai')
#HelloName('Miya')

#函数2：打印两个数相加
def add(a, b): 
    s = "%s + %s = %s"
    print(s % (a, b, a+b))
    
#add(1, 2)
#add('Hello', ' Kevin')

#函数3：打印两个数相减的结果
def sub(q, w):
    r = '%s - %s = %s'
    print(r %(q, w, q - w))

#sub(9, 4)

#函数4：打印两个数相乘.用函数打印字符串
def mul(e, t):
    y = "%s * %s = %s"
    print(y %(e, t, e * t))

#mul(5, 7)
#mul('Kevin ', 10)

#函数五：写1个函数反回它们的和
def add2(a, b):  
    c = a + b
    return c
     
x = add2(66, 6)
print(x)

#函数六：写1个函数反回两的      
def sub2(d, l):
    r = d - l
    return r
    
r = sub2(35, 7)
print(r)

#函数7：写1个函数反回它们的积
def mul2(r, z):
    y = r * z
    return y
y = mul2('Kevin ', 10) 
print(y)

#函数8：从1加到n
def add_to(n):
    r = 0
    for y in range(n):
        r = r + y + 1
        print(r)
    return r

add_to(100)