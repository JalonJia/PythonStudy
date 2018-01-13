s_sum = "0加到%s 的和是：%s"
i_sum = 0
for i in range (1, 101):
    print("i的值：%s" % i)
    _sum = i_sum + i
    print(s_sum % (i, i_sum))
    
s_atoz = 'abcdefghijklmnopqrstuvwxyz'
s_atoz2 = 'abcdefghijklmnopqrstuvwxyz'
for s in (s_atoz):
    print(s*2)  #字符串乘法
    print(s + s_atoz2) 
    

s_Home = '''"It's a %s, I like it!", %s said yesterday.'''
print(s_Home % ('一家人', 'Kevin'))
print(s_Home % ('Mather', 'Miya'))
print(s_Home % ('computer', 'jalon'))