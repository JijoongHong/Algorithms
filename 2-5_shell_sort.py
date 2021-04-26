def shell_sort(arr):

    h = len(arr) // 2
    while h > 0:
        for i in range(h, len(arr)):
            t = arr[i]
            j = i
            # insertion sort
            while j >= h and arr[j-h] > t:
                arr[j] = arr[j-h]
                j -= h
            arr[j] = t
            print(arr)


        h = h // 2
        print(h)
        print("__________________________")

    return arr

arr = [3, 4, 1, 5, 6, 7, 2, 9, 8, 3, 1, 6, 4]
print(shell_sort(arr))
print(len(arr))