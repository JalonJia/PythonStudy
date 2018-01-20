#求1+2+3+。。。+100的和
total = 0
for i in range(100):
    #print(i)
    total = total + i + 1
    
print(total)

total = 0
for i in range(200):
    total = total + i + 1
    
print(total)

total = 1
for i in range(100):
    total = total * (i+1)

print("100的阶乘：")
print(total)



def calcSum(n):                 
    mTotal = 0
    for i in range(n):
        mTotal = mTotal + (i+1)
    print(mTotal)



calcSum(100)
calcSum(200)
calcSum(300)    

