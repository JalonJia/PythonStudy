'''
Created on 2018年12月16日

@author: KKVV
'''

import math 

class Point:
    """
    x
    y
    """

        
    
class Circle:
    """
    center
    radius
    """

#实例化对象
j = Circle()
j.center = Point()
j.radius = 75
j.center.x = 150
j.center.y = 100


p = Point()
p.x = 150
p.y = 175

a = p.y - j.center.y
b = p.x - j.center.x
c = math.sqrt(a**2 + b**2)
print(c)
if c <= j.radius:
    print(f'Point({p.x}, {p.y})在圆里面')
else:
    print(f'Point({p.x}, {p.y})不在圆里面')
    