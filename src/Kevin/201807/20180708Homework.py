'''
作业: 关于列表的一些计算
1. 《像计算机科学家一样思考Python》第10章看一遍，不会的拿铅笔画出来
2. 完成《像计算机科学家一样思考Python》第105页练习10-1
3. 完成《像计算机科学家一样思考Python》第105页练习10-2
3. 完成《像计算机科学家一样思考Python》第106页练习10-3
3. 完成《像计算机科学家一样思考Python》第106页练习10-4
3. 完成《像计算机科学家一样思考Python》第106页练习10-5
'''

#2. 完成《像计算机科学家一样思考Python》第105页练习10-1
def nested_sum(e):
    w = 0
    for i in range(len(e)):
        w = w + e[i]
    print(w)
#nested_sum(e = [[1, 2], [3], [4, 5, 6]])
 
def middle(r):
    u = []
    for i in range(len(r)):
        if i == r[0] or i == len(r) - 1:
            continue
        u.append(r[i])
    print(u)
    return u
middle(r = [1, 2, 3, 4, 5, 6, 8])
#3. 完成《像计算机科学家一样思考Python》第105页练习10-2
def cumsum(t):
    j = []
    r = 0
    for i in range(len(t)):
        print(i)
        r += t[i]
        j.append(r)
    print(j)
    r += 1
t = [100, 1, 2, 3]
cumsum(t)    

def chop(t):
    for i in range(len(t)):
        if (i == 0) or (i == len(t) - 1):
        
            t.remove(t[i])
    print(t)
chop(t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def is_sored(h):
    if len(h) <= 1:
        print(True)
        return True
    for i in range(len(h) - 1):
        if h[i] > h[i + 1]:
            print(False)
            return False
    
is_sored(h = [9, 8, 7, 6, 5, 4, 3, 2, 1])