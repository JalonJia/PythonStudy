'''
TODO: 打印乘法口诀表
'''
j = 1
k = 1
for i in range(9):
    #print(h * k )
    for n in range(k):
        j = n + 1
        l = j * k
        h = '%d * %d = %d ' % (j, k, l)
        print(h, end=' ')    
    print('')    
    k = k + 1
      

    
    