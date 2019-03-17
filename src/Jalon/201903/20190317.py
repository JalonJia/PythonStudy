import copy

class Time:
    """
    定义时间的类
    参数有：hour，minute，second
    seconds:总时间
    """
    def __init__(self, hour = 9, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        #print('Time.__init__')
    
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second))
        
    def time_to_int(self):
        seconds = self.hour * 3600 + self.minute * 60 + self.second
        return seconds

    def int_to_time(seconds):
        new_time = Time()
        new_time.hour = int(seconds/3600)
        new_time.second = seconds%60
        new_time.minute = (seconds%3600 - new_time.second) / 60
        return new_time
        
    def increment(self, seconds):
        '''
        方法用来对现在的时间增加指定的秒数
        '''
        seconds += self.time_to_int()
        return Time.int_to_time(seconds)        
    
    def is_after(self, t2):
        """
        比较两个时间，如果t1在t2之后，返回True，否则返回False
        """
        return ((self.hour > t2.hour) 
                or ((self.hour == t2.hour) and (self.minute > t2.minute))
                or ((self.hour == t2.hour) and (self.minute == t2.minute) and (self.second > t2.second)))


start = Time()
start.hour = 7
start.minute = 45
start.second = 0

#print_time(start)
Time.print_time(start)#基本不用

start.print_time() #对象.方法()

end = start.increment(300)
end.print_time() #对象.方法()

print(end.is_after(start))

test = Time(7, 45,56)
test.print_time()

