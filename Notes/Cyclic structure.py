# while cond:
#     block

a = 0
while a < 10:
    print("while:",a)
    a += 1

# 通常在While循环中，循环体中需要修改条件，以使得条件为假。

# for element in itrator:
#     block
a = range(0,10)
for b in a:
    print("for:",b)
# 循环体中绝对不要修改可迭代对象

#修改实验,极度危险，笑脸！
#程序挂掉，或者机器挂掉。

# lst = range(0,10)
# for i in lst:
#     lst.appd(i)

# 选择结构与循环结构的嵌套
for i in range(0,10):
    if i % 2 == 0:
        print("if.for :",i)

# Stop Cyclic
# Break 结束循环
for i in range(0,10):
    if i > 3:
        break
    print("break:", i)

# Jump Cyclic
# Cotinue 跳过之后的语句
for i in range(0,10):
    if i == 3:
        continue
    print("cotinue:",i)

# 求素数
a = 6
c = 5
for i in range(2,a):
    print("i:",i)
    print("c:",c)
    if a % i == 0:
        print("break:")
        break
    c += 1

if c < a - 2:
    print("no")
else:
    print("yes:")

# 循环结构中 else 子句判断循环是否提前退出，如果提前退出了，else子句不执行，如果没有提前退出，执行else子句。
a = 5
for i in range(2,a):
    if a % i == 0:
        break
else:
    print("yes")

is_break = False
for i in range(0,10):
    for x in range(0,10):
        if x >= 4:
            is_break = True
            break
        print('x: {0}'.format(x))
    else:
        print("i: {0}".format(i))
    if is_break:
        break