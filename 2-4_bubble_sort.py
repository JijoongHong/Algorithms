def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        changed = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                print(j,":", arr[j], "/",j+1, ":",arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(j,":", arr[j], "/",j+1, ":",arr[j+1])
                print(arr)
                print("---------------------")
                changed = True
        if not changed:
            break

    return arr

arr = [1,3,2,6,3,1,4,6]
arr = bubble_sort(arr)
print(arr)