#####
#
#内容来自：http://www.yulongjun.com/python/20170511-01-function-define/
#
#####

#定义函数（define）
#简单的定义一个函数的格式：
# def function_name(parameter_list):
#     statements

#结构为def，后面接函数名(function name)，然后括号括起来的参数列表（parameter list），参数以逗号分隔，然后再接冒号:，下面是函数语句(statements)。
#函数语句里通常包含一个return语句，或者是yield语句，或者是二者都有。
#写一个简单的函数：
def add(x,y):
    return x+y
print("add: 1+2={}".format(add(1,2)))
 