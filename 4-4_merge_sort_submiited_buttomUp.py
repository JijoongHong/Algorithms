def merge_sort_bu(arr):
    size = 1
    n = len(arr)
    while size < n:
        get_idx(arr, size, n)
        size = size * 2

    return arr


def get_idx(arr, size, n):
    lo1 = 0
    while lo1 + size < n + 1:
        hi1 = lo1 + size - 1
        lo2 = lo1 + size
        hi2 = lo2 + size - 1

        if hi2 >= n:
            hi2 = n - 1

        merge2(arr, lo1, hi1, lo2, hi2)
        lo1 = hi2 + 1


def merge2(arr, lo1, hi1, lo2, hi2):
    i = lo1
    j = lo2
    temp = []

    while i <= hi1 and j <= hi2:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1

        else:
            temp.append(arr[j])
            j += 1

    while i <= hi1:
        temp.append(arr[i])
        i += 1

    while j <= hi2:
        temp.append(arr[j])
        j += 1

    for i in range(len(temp)):
        arr[lo1+i] = temp[i]

    print("size({0}) | merged data : {1} | current state : {2}".format((hi1-lo1+1), temp, arr))


if __name__ == "__main__":
    a = [15, 14, 32, 12, 7, 25, 8, 6, 3]
    print('initial :', a)
    print('--------------------------------------------------------------------------------------------------------------')
    a2 = merge_sort_bu(a)
    print('--------------------------------------------------------------------------------------------------------------')
    print('sorted :', a2)
