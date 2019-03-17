class People:
    '''
    定义：人
    '''
    
kevin = People()
kevin.name = '贾继开'
kevin.age = 10
kevin.height = 24

print(People)
print(kevin)

print(kevin.name)

def set_name(people, name):
    '''
    修改器
    设置一个People对象的名字
    '''
    people.name = name
    
Miya = People()
set_name(Miya, '贾淼淼')
Miya.age = 8

print(Miya.name)

def calc_age_delta(people1, people2):
    '''
    纯函数
    计算两个People的年龄差
    '''
    return people1.age - people2.age

print(calc_age_delta(kevin, Miya))


