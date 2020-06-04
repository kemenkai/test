#####
#
#内容来自：http://www.yulongjun.com/python/20170510-07-iterables-interators-generators-verbose/
#
#####
list1_1 = []
for i in range(6):
    list1_1.append(i)
print('list1_1: {}'.format(list1_1))
list1_2 = [i for i in range(6)]
print('list1_2: {}'.format(list1_2))

list2_1 = []
for i in range(6):
    if i % 2 == 1:
        list2_1.append(i)
print('list2_1: {}'.format(list2_1))
list2_2 = [i for i in range(6) if i % 2 == 1]
print('list2_2: {}'.format(list2_2))

list3_1 = []
for i in range(6):
    if i % 2 == 1:
        if i > 2:
            list3_1.append(i)
print('list3_1: {}'.format(list3_1))
list3_2 = [i for i in range(6) if i % 2 == 1 if i > 2]
print('list3_2: {}'.format(list3_2))

# 笛卡尔积
list4_1 = [1,3,4]
list4_2 = [2,4,6]
list4_3 = []
for x in list4_1:
    for y in list4_2:
        list4_3.append((x,y))
print('list4_3: {}'.format(list4_3))
list4_4 = [(x,y) for x in list4_1 for y in list4_2]
print('list4_4: {}'.format(list4_4))

# zip()
uppers = ['A','B','C']
lowers = ['a','b','c']
nums = ['1','2','3']
print('zip: {}'.format(zip(uppers,lowers,nums)))
print('list_zip: {}'.format(list(zip(uppers,lowers,nums))))

# 集合解析式
set1 = {2,2,2}
print("set1: {}".format({x+1 for x in set1}))

# 字典解析式
letters = ['A','B','C','D']
nums = [1,2,3,4]
dict = {k:v for k,v in zip(letters,nums)}
print('dict: {}'.format(dict))

# 生成器解析式,生成器只能迭代一次，迭代完就空了
gen1 = (i for i in range(6))
print('gen_type: {}'.format(type(gen1)))
list5_1 = list(gen1)
print('gen_list5_1: {}'.format(list5_1))
list5_2 = list(gen1)
print('gen_list5_2: {}'.format(list5_2))