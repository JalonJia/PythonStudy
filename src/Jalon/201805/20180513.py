'''
TODO: 打印乘法口诀表
'''

a = 1
b = 1
c = a*b
s1 = '%d*%d=%d' % (a, b, c)

a = 1
b = 2
c = a*b
s2_1 = '%d*%d=%d' % (a, b, c)
a = a + 1
b = 2
c = a*b
s2_2 = ' %d*%d=%d' % (a, b, c)
s2 = s2_1 + s2_2

#s3 = '1*3=3 2*3=6 3*3=9'
a = 1
b = 3
c = a*b
s3_1 = '%d*%d=%d' % (a, b, c)
a = a + 1
b = 3
c = a*b
s3_2 = ' %d*%d=%d' % (a, b, c)
a = a + 1
b = 3
c = a*b
s3_3 = ' %d*%d=%d' % (a, b, c)
s3 = s3_1 + s3_2 + s3_3

#print(s1)
#print(s2)
#print(s3)

#n的乘法口诀
def n_mul(n):
    s_temp = '%d*%d=%d' % (n, n, n*n)
    len_max = len(s_temp)
    for i in range(n):
        s = ''
        for x in range(i + 1):
            a = x + 1
            b = i + 1
            c = a * b
            s1 = '%d*%d=%d' % (a, b, c)
            if len(s1) < len_max:
                s1 = s1 + ' '*(len_max-len(s1))
                
            if s != '' :
                s = s + ' ' + s1
            else:
                s = s1
                
        print(s)


n_mul(n = 100)




