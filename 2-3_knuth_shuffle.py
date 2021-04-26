import random

def shuffle(arr):
    random.seed(10)
    for i in range(len(arr)):
        rand = i + random.randint(0,len(arr)-1-i) # range of rand is i<=r<=n-1
        print(i, rand)
        print(arr[i], arr[rand])
        arr[i], arr[rand] = arr[rand], arr[i]
        print(arr[i], arr[rand])
        print("-------------------")


    return arr

arr = [1, 2, 3, 4, 5]
print(shuffle(arr))