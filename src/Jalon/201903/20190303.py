import copy

class Time:
    """
    定义时间的类
    参数有：hour，minute，second
    """
    
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second))



def is_after(t1, t2):
    """
    比较两个时间，如果t1在t2之后，返回True，否则返回False
    """
    return ((t1.hour > t2.hour) 
            or ((t1.hour == t2.hour) and (t1.minute > t2.minute))
            or ((t1.hour == t2.hour) and (t1.minute == t2.minute) and (t1.second > t2.second)))


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

#print_time(start)
Time.print_time(start)#基本不用

start.print_time() #对象.方法()

