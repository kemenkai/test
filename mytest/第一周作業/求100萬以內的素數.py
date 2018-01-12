num = 1000000
for i in range(2,num):
    for a in range(2,i-1):
        if i % a == 0:
            break
    else:
        print(i)


# def test2():
#     num = 1000000
#     for i in range(2,num):
#         if i == 2 or i == 3:
#             print(i)
#         elif i % 2 == 0 or i % 3 == 0:
#             continue
#         else:
#             print(i)
# test2()