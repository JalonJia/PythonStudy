import copy
from cmath import rect

class Point:
    """
    坐标
    属性：x，y
    """
    
class Rectangle:
    """
            矩形
    属性：左下角的坐标，宽度，高度
    """
    
rect = Rectangle()
rect.corner = Point()
rect.corner.x = 3.0
rect.corner.y = 4.0
rect.width = 200.0
rect.height = 100.0

def find_center(box):
    p = Point()
    p.x = box.corner.x + box.width/2
    p.y = box.corner.y + box.height/2
    return p

def print_point(p):
    print('(x:%g, y:%g)' % (p.x, p.y))


center = find_center(rect)
print_point(center)

rect.height += 50
rect.width += 100
center = find_center(rect)
print_point(center)

print('rect.heitht: %s' % rect.height)
rect2 = rect
rect2.height += 100
print('rect.heitht after: %s' % rect.height)

#浅拷贝
rect3 = copy.copy(rect)
rect3.height +=99
print('rect.heitht after copy: %s' % rect.height)
print(rect)
print(rect2)
print(rect3)

#print(rect.corner.x)
#rect3.corner.x += 50
#print(rect.corner.x)

#深拷贝，完全拷贝
rect4 = copy.deepcopy(rect)
rect4.corner.x += 50
rect4.corner.x -= 50
print(rect.corner.x)

#判断两个对象是否相同的对象使用 is
#判断两个对象的属性是否相同使用 ==
print(rect4 is rect)
rect5 = copy.copy(rect)
print(rect5.corner is rect.corner)
print(rect4.corner.x == rect.corner.x)


#使用函数isinstance(object, class)来判断某个实例是否是某个类的实例
print(isinstance(rect, Rectangle))
print(isinstance(rect4.corner, Point))
#print(isinstance(rect4.corner.x, float))

#判断一个实例是否包含拥有某个属性使用函数hasattr(object, 'attribute_name')
print(hasattr(rect, 'corner'))
print(hasattr(rect, 'height'))
print(hasattr(rect, 'x'))
print(hasattr(rect.corner, 'x'))



