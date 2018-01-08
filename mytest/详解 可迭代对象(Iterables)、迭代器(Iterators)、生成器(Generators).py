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
class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
f = fib()
print("list(islice(f10,10)): {}".format(list(islice(f,0,10))))
#print("list(islice(f10,10)): {}".format(list(f))) # 会无限迭代，直接死机
#请注意，这个类即是一个iterable（因为它运行一个__iter__() 方法），也是迭代器（因为它有一个__next__()方法）。
#这个iterator中的状态完全保存在内部的prev和curr实例变量中，并用于后续调用迭代器。每一次调用next()都要做两件重要的事情：
#修改状态，为了下一次调用next()做准备。
#生成当前调用的结果。
#中心思想：一个懒惰的工厂
#从外面看，interator就像一个懒惰的工厂，平常是空闲的，除非你向它请求一个值，他才会产生一个单个的值，然后再次进入空闲状态，直到你下次再调用，这样循环往复。



# 生成器（Generators）
#最后，我们终于要说generator了！generator是我最爱的Python语言功能。一个generator就是一个特殊的迭代器——优雅的那种。
#一个生成器允许你像上面的斐波纳契序列迭代器示例一样，来编写迭代器，但是使用了一个优雅的简洁语法，避免在类里写__iter__()和__next__()方法。
#让我们明确的说一下：
#任何generator也是一个iterator（反之亦然！）;
#因此，任何generator也是一个惰性生成值的工厂。
#下面也是一个斐波那契序列工厂，但是是用generator写的：
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

f = fib()
print("list(islice(f,0,10))2: {}".format(list(islice(f,0,10))))
#让我们分解一下这里发生的一切：首先要注意的fib是一个普通的Python函数，没什么特别的。但是，请注意，在函数体里没有return关键字。函数的返回值将是一个generator（心中默念：一个iterator，一个懒惰的工厂，一个有状态的帮助对象）。
#现在，当f = fib()被调用时，genrator（懒惰的工厂）被实例化并返回，此时不会执行任何代码：只是启动了一个初始化状态的空闲generator。要明白一点：prev, curr = 0, 1这行代码还没有被执行。
#然后，这个generator实例被包在一个islice()函数里。lslice(f,0,10)本身也是一个迭代器，最初是空闲的。还是什么都没有发生。
#然后，这个迭代器被包装在一个list()函数里，它将消耗它的所有参数，并从它构建一个列表。为了做到这一点，它将开始在islice()实例里调用next() ，这其实是转向f实例里调用next()。
#但是一次只有一步。在第一次调用时，代码会最终运行一点：prev, curr = 0, 1这行执行了，然后再到while True循环开始，然后遇到yield curr语句。然后会生成一个值，这个是就是当前curr变量里的值，然后再次进入空闲状态。
#这个产生的值传入到islice()，list()函数可以把第一次生成的值1加入到列表里。
#因为还没到第10个，这时会要求islice()下一个值，然后传递到要求f下一个值，它将f从之前的状态“取消暂停” ，接着运行prev, curr = curr, prev + curr。然后再次进入while循环的下一次迭代，并且命中yield curr语句，返回下一个curr的值2。
#直到输出列表为10个元素长度，这时list()要求 islice()第11个值时，islice()会引发StopIteration异常，表示已到达结束，并且列表将返回结果：10个项目的列表，其中包含了前10个斐波纳契数。请注意，generator不接收第十一个next()的调用。实际上，它不会再被使用了，之后会被垃圾回收。

# 生成器类型（Types of Generators）
#Python中有两种类型的generator：generator函数（function）和generator表达式(expression)。只要yield在其函数体内出现，就叫generator函数。我们刚才还看了一个例子就是这样的。关键字的yield的出现足以使函数成为generator函数。
#假设你用下面的列表解析式（list comprehension）语法来构建一个平方数列
numbers1 = [1,2,3,4,5,6]
print("numbers1: {}".format([x * x for x in numbers1]))
#你可以用集合解析式(set comprehension)来做相同的事情：
print("numbers2: {}".format({x * x for x in numbers1}))
#或者是一个字典解析式(dict comprehension)：
print("numbers3: {}".format({x: x * x for x in numbers1}))
#但是您也可以使用生成器表达式（generator expression）（注意：这不是一个元组解析式(tuple comprehension），没有元组解析式这种东西）
lazy_squares = (x * x for x in numbers1)
print("lazy_squares_type: {}".format(type(lazy_squares)))
print("lazy_squares: {}".format(next(lazy_squares)))
print("lazy_squares_list: {}".format(list(lazy_squares)))
#需要注意的是，因为我们用next()方法从lazy_squares读入第一个值，状态目前在第二个item上，所以，当我们通过调用list()来消费所有元素时，只会从第二个开始读入，因为我们已经用next()消费了一个了。（这也向我们展示了惰性求值行为）。这也是一个和上面例子一样的generator（当然了，也是iterator）

#generator是一个不可思议的强大的编程结构。它们允许您编写具有较少中间变量和数据结构的流式代码。除此之外，它们具有更高的内存和CPU效率，他们也用更少的代码行来书写。
#开始使用generator。
#在代码中找到如下位置：
# def something():
#     result = []
#     for ...in ...:
#         result.append(x)
#     return result
# #并替换为：
# def iter_something():
#     for ...in...:
#         yield x
# return list(iter_something())
