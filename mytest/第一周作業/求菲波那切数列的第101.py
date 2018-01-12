def test1(n):
    stack = []
    if n == 0 or n == 1:
        return 1
    else:
        stack.append(0)
        stack.append(1)
        for i in range(2,n):
            stack.append(stack[i-1]+stack[i-2])
    return stack
print(test1(1000))

def test2(n):
    x,y = 0,1
    result = []
    while y<n:
        result.append(x)
        x,y = y, x+y
    return result
print(test2(10000))

import itertools
def test3():
    x,y = 0,1
    while True:
        yield x
        x,y = y,x+y

print(list(itertools.islice(test3(),1000)))
