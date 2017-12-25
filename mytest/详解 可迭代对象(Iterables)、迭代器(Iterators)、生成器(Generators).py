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
# keys
d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d
assert 4 not in d
assert 'foo' not in d # 'foo' is not a _key_ in the dict
# str
s = 'foobar'
assert 'b' in s
assert 'x' not in s
assert 'foo' in s # a string "contains" all its substrings

#