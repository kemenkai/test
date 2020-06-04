#####
#
#内容来自：http://www.yulongjun.com/python/20170510-07-iterables-interators-generators-verbose/
#
#####
#可迭代对象（iterable）
#列表、元组、集合、字典、字符串、bytes、bytearray、生成器（generator）、range等，都是可迭代对象（iterable）。
#简单的可以这样理解：能用for...in循环来迭代、能用in成员运算符的，都是可迭代对象。


#迭代器（iterator）
#通过iter函数，可以把可迭代对象（iterable）封装成为迭代器（iterator）。
#迭代器的本质是一种封装。
#很多地方都隐式的调用了迭代器。for…in循环和成员运算符隐式的调用了iter函数。
r = range(3)
it = iter(r)
print('type_ir: {}'.format(type(it)))
print('type_r: {}'.format(type(r)))
print('\n')

#next函数可以迭代迭代器。
#当迭代器没有下一个元素的时候，next函数会抛出StopIteration异常。
#没有下一个元素的时候，如果设置了默认返回值，迭代结束就不会抛出异常，而是返回默认返回值。
print('netx_it0: {}'.format(next(it)))
print('netx_it1: {}'.format(next(it)))
print('netx_it2: {}'.format(next(it)))
# print('netx_it3: {}'.format(next(it)))
print('\n')


#生成器（generator）
#生成器（generator）是迭代器的子集（iterator），迭代器中包含了生成器。
#生成器可以用上节的生成器解析式来生成。
#由于生成器也是迭代器，所以也可以使用next方法。
g = (x for x in range(3))
print('type_g: {}'.format(type(g)))
print('netx_g0: {}'.format(next(g)))
print('netx_g1: {}'.format(next(g)))
print('netx_g2: {}'.format(next(g)))
# print('netx_g3: {}'.format(next(g)))
print('\n')

