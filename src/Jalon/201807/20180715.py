#10-2
def cumsum(t):
    result = []
    sum = 0
    for x in t:
        sum += x
        result.append(sum)
    
    print(f'结果是{result}')
    return result

t = [1, 2, 3]
cumsum(t)

#10-3
def middle(t):
    result = []
    for i in range(len(t)):
        if (i == 0) or (i == len(t) - 1):
            continue
        
        result.append(t[i])
    
    print(f'新列表是{result}')
    return result

t = [1,2,3,4]
middle(t)
print(t)

#10-1
def nested_sum(t):
    result = 0
    for x in t:
        if type(x) == list:
            for y in x:
                
                result += y
        elif type(x) == int:
            result += y
     
    print(f'列表中所有数字的和是{result}')
    return result

t = [[1,2], [3], [4,5,6]]
nested_sum(t)

#10-4
def chop(t):
    for i in range(len(t)):
        if (i == 0) or (i == len(t) - 1):
            t.remove(t[i])

t = [1,2,3,4]
chop(t)
print(f'修改后列表是{t}')       

#10-5
def is_sorted(t):
    last = None    
    for x in t:
        if last == None:
            last = x
        elif last > x:
            print(f'列表{t}不是升序')
            return False
        else:
            last = x
    
    print(f'列表{t}是升序')
    return True

t = [1,2,3,4]
is_sorted(t)

t = [1,2,3,4,6,5]
is_sorted(t)

        

