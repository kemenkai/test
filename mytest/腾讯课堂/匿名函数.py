# 匿名函数
# 使用 lambda 定义匿名函数
# 实例1：
print(lambda x: x+1)
print("匿名函数执行方法1：(lambda x: x+1)(3)")
print((lambda x: x+1)(3))
# 匿名函数的特点：
# 1 lambda 来定义
# 2 参数列表不需要用小括号
# 3 冒号不是用来开启新的语句块
# 4 最后一个表达式没有 return 语句，最后一个表达式的直即返回值

# 匿名函数实例解析，第一对括号为改变优先级，第二对括号为行数对象是以括号调用的
(lambda x: x+1)(3)

# 实例2
# 匿名函数（lambda表达式）只能写在一行上，所以也有叫它单行行数
# f = lambda x: if x< 0:
#     0
# else:
#     x

# 实例3
# 匿名函数没有参数也是可以的
print((lambda :0)())

# 实例4
# 多个参数OK
print((lambda x,y: x + y)(3,5))

# 实例5
# 默认参数OK
print((lambda x,y=3: x + y)(2))

# 实例6
# 可变参数OK
print((lambda *args: args)(*range(3)))

# 实例7
# 两种可变参数OK
(lambda *args,**kwargs: print(args,kwargs))(*range(3),**{str(x):x for x in range(3)})

# 实例8
# 关键字参数
(lambda *, x: print(x))(x=3)

# 普通函数所支持的参数变化，匿名函数都支持


# 对可迭代对象做排序
help(sorted)


# 实例9
from collections import namedtuple
User = namedtuple('User',['name','age'])
users = [User('kmk1',18),User('kmk2',16),User('kmk3',14)]
def get_age(user):
    return user.age
print(sorted(users,key=get_age))
print(sorted(users,key=lambda x:x.age))




# 实例10
help(map)
print(list(map(lambda x: x.age, users)))

# 实例11
help(filter)
print(list(filter(lambda x:x.age < 30, users)))

# 匿名函数通常用于高阶函数的参数，当此函数非常短小的时候，就适合使用匿名函数

# map函数的实现
def map_(fn,it):
    return (fn(x) for x in it)

# filter函数的实现
def filter_(fn,it):
    return (x for x in it if fn(x))