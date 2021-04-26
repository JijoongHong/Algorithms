def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr

arr = [1,3,2,6,3,1,4,6]
arr = selection_sort(arr)
print(arr)