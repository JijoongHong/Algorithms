count = 0
l = [1,2,3,4,5,6]
i = 0
j = 0
k = 0
n = 6
#for n in l:
for i in range(0, n):
    print("----------")
    print("i",i)
    for j in range(i+1, n):
        print("j",j)
        for k in range(j+1, n):
            print("k",k)
            #print(k)
            count += 1


print("----------")

print(count)

#print(i, j, k)


# 1 -> 0
