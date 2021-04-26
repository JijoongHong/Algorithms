def lsd_sort(arr):
    width = 3
    n = len(arr)
    r = 128
    temp = [None] * n
    for d in reversed(range(width)):
        count = [0] * (r+1)
        for i in range(n):
            count[ord(arr[i][d]) + 1] += 1
        for j in range(1, r):
            count[j] += count[j-i]
        for i in range(n):
            p = ord(arr[i][d])
            temp[count[p]] = arr[i]
            count[p] += 1
        for i in range(n):
            arr[i] = temp[i]
        for x in arr: print(x, " ", end='')
        print()

a = [26, 28, 38, 39, 62, 72, 81, 93]
lsd_sort(a)
