import copy

class Time:
    """
    定义时间的类
    参数有：hour，minute，second
    """
    

def print_time(h):
    print('%.2d:%.2d:%.2d'%(h.hour, h.minute, h.second))

def is_after(t1, t2):
    """
    比较两个时间，如果t1在t2之后，返回True，否则返回False
    """
    return ((t1.hour > t2.hour) 
            or ((t1.hour == t2.hour) and (t1.minute > t2.minute))
            or ((t1.hour == t2.hour) and (t1.minute == t2.minute) and (t1.second > t2.second)))
            
#     if t1.hour > t2.hour:
#         return True
#     
#     if (t1.hour == t2.hour) and (t1.minute > t2.minute):
#         return True
#     
#     if (t1.hour == t2.hour) and (t1.minute == t2.minute) and (t1.second > t2.second):
#         return True
#     
#     return False
    
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    
    return sum

def increment(t1, seconds):
    t1.second += seconds
    
    t1.minute += int(t1.second/60)
    t1.second = t1.second % 60
    
#     while t1.second >= 60:
#         t1.second -= 60
#         t1.minute += 1
    
    while t1.minute >= 60:
        t1.minute -= 60
        t1.hour += 1

def increment2(t1, seconds):
    sum = Time()    
    sum = copy.deepcopy(t1)
    
    increment(sum, seconds)
    
    return sum
    
    
time = Time()
time.hour = 12
time.minute = 30
time.second = 0

time1 = Time()
time1.hour = 12
time1.minute = 30
time1.second = 0


print_time(h = time)
print_time(h = time1)
time2 = add_time(time, time1)
print_time(time2)

increment(time, 9810)
print_time(h = time)

time3 = increment2(time, 9810)
print_time(h = time)
print_time(time3)

print(is_after(time1, time))



#def time(j, k, l):
    