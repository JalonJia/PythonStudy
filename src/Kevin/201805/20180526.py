j = 1
k = 1
for i in range(10):
    for u in range(k):
        j = u + 1
        l = j * k
        f = '%d * %d = %d '%(j, k, l)
        print(f, end = (' '))
    k = k + 1    
    print(' ')