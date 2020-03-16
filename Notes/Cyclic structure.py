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