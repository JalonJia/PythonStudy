
class Time:
    '''
    hour
    minute
    second
    '''

def mul_Time(day, t):
    x = Time()
    x.hour = t.hour * day
    x.minute = t.minute * day
    x.second = t.second * day
    while x.second >= 60:
        x.second -= 60
        x.minute += 1
    
    while x.minute >= 60:
        x.minute -= 60
        x.hour += 1
    
    #print('%.2d:%.2d:%.2d' % (x.hour, x.minute, x.second))    
    return x

def print_time(x):
    print('%.2d:%.2d:%.2d' % (x.hour, x.minute, x.second)) 

if __name__ == '__main__':
    tm = Time()
    tm.hour = 0
    tm.minute = 30
    tm.second = 20
    print_time(tm)
    days = 8
    tot = mul_Time(days, tm)
    print_time(tot)
