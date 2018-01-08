#####
#
#内容来自：http://www.yulongjun.com/python/20170510-07-iterables-interators-generators-verbose/
#
#####
# 容器（Containers）
# 容器是指存有元素的数据结构，支持成员测试。容器是存在内存里的数据结构，通常它们的值也在内存里。在Python里内置的容器有：
#
# list, deque, …
# set, frozensets, …
# dict, defaultdict, OrderedDict, Counter, …
# tuple, namedtuple, …
# str
# 容器易于掌握，因为您可以将其视为现实生活中的容器：盒子，立方体，房屋，船舶等。
#
# 从技术上讲，一个对象是一个容器，可以询问它是否包含某个元素。您可以对列表，集合或元组执行这样的成员关系测试：
# lists
assert 1 in [1,2,3]
assert 4 not in [1,2,3]
# sets
assert 1 in {1,2,3}
assert 4 not in {1,2,3}
# tuples
assert 1 in (1,2,3)
assert 4 not in (1,2,3)
# dict
d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d
assert 4 not in d
assert 'foo' not in d # 'foo' is not a _key_ in the dict
# str
s = 'foobar'
assert 'b' in s
assert 'x' not in s
assert 'foo' in s # a string "contains" all its substrings

# 可迭代对象（Iterables）
#如上所述，大多数容器也是iterable，但是还有更多的东西是iterable，比如说打开的文件，打开的套接字（sockets）等。容器通常是有限的；iterable可以是有限的，也可以表示无限的数据源。
#iterable不只可以是数据结构，也可以是能返回迭代器（Iterator）的任何对象（目的是为了返回其中的元素）。听起来有一点绕，但iterable和iterator有一个重要的不同，我们来看例子更明了：

x = [1,2,3]
y = iter(x)
z = iter(x)
print("next(y): {}".format(next(y)))
print("next(y): {}".format(next(y)))
print("next(z): {}".format(next(z)))
print("type(x): \n{}".format(type(x)))
print("type(y): \n{}".format(type(y)))

import dis
x = [1,2,3]
dis.dis('for _ in x: pass')

# 迭代器（Iterators）
#那么什么是 iterator 呢？它是一个有状态的帮助对象，当您调用 next() 时将生成下一个值。因此，任何具有__next__()方法的对象都是iterator，如何生成一个价值是无关紧要的。
#所以迭代器是一个生产值的工厂。每次你要求它的“下一个”值，它知道如何计算它，因为它保存内部状态。
#有无数的迭代器例子。所有的itertools函数都返回iterator。
#有些生成无限序列(infinite sequences)：
from itertools import count
counter = count(start=13)
print('next(counter)1: {}'.format(next(counter)))
print('next(counter)2: {}'.format(next(counter)))

#有些生成从有限序列（finite sequences）生成无限序列：
from itertools import cycle
colors = cycle(['red','white','blue'])
print("next(colors)1: {}".format(next(colors)))
print("next(colors)1: {}".format(next(colors)))
print("next(colors)1: {}".format(next(colors)))
print("next(colors)1: {}".format(next(colors)))

#有些从无限序列生成有限序列：
from itertools import islice
colors = cycle(['red','white','blue'])
limited = islice(colors,0,3)
for x in limited:
    print("x: {}".format(x))

#为了更好地了解interator的内部结构，我们来构建一个产生斐波那契数的interator：

