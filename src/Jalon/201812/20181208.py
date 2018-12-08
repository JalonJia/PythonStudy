import math 

class Point:
    '''
            定义一个类
    
    '''
    def __init__(self):
        '''
                        初始化类
        '''
        self.x = 0
        self.y = 0
    

print(Point)

blank = Point()

print(blank)
'''
print(int)
print(str)
print(dict)

a = int()
print(a)
'''

blank.x = 3.0
blank.y = 4.0
#blank.z = 1
x = blank.x

print(blank.x)
print(blank.y)
#print(blank.z)
print(x)

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


print_point(blank)

def distance_point(p):
    c = math.sqrt(p.x**2 + p.y**2)
    return c
    
z = distance_point(blank)
print(z)



