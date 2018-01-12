num = 1000
for i in range(2,num):
    for a in range(2,i):
        if i % a == 0:
            break
    else:
        print(i)

