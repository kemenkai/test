num = 10000
num2 = 0
for i in range(2,num):
    for a in range(2,int(i ** 0.5)+1):
    # for a in range(2,i):
        if i % a == 0:
            break
    else:
        #print(i)
        num2 += 1
print(num2)