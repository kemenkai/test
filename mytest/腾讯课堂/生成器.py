# 生成器解析
# 实例1
def g():
    for x in range(10):
        yield x # 表示弹出一个值
r=g() # 函数已经执行完成，函数的现场应该已经被销毁
print(next(r))
for i in r:
    print(i)

# 实例2
def gen():
    print('a')
    yield 1
    print('b')
    yield 2
    return 3
g = gen() # 执行生成器函数的时候，函数体并没有被执行
print(next(g)) # 执行到第一个 yield ，停止执行了
print(next(g)) # 从第一个 yield 之后开始执行，在第二个 yield 的时候停止
# print(next(g)) # 抛出异常，从第二个 yield 开始执行，当没有更多 yield 的时候，抛出 STopIteration 异常，异常的值正好是返回值
# 带 yield 语句的函数称之为生成器函数
