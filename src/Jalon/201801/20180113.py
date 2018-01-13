
"""
if ... else的使用
"""
"""
计算0 + 2 + 4 + 6 +8 + 10 + 。。。 + 100的结果
"""
e = 0
for r in range(1, 101):
    if r % 2 == 0: #表示是偶数/双数
        e = e + r
#    else #r是单数/奇数
#        e = e + r
print(e)

"""
计算0 + 1 + 3 + 5 + 7 + 9 + 。。。 + 99的结果
"""
e = 0
for r in range(1, 100):
    if r % 2 == 1: #表示是单数/奇数
        e = e + r

print(e)

"""
判断n能不能被m整除
"""
def is_divisible(n, m):
    if n % m == 0: #n能被m整除
        print('%s能被%s整除' % (n, m))
    else:
        print('%s不能能被%s整除, 余数是：%s' % (n, m, n%m))
    

is_divisible(n = 100, m = 30)
is_divisible(n = 81, m = 9)


    