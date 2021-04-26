def merge_sort_bu(arr):
    size = 1
    n = len(arr)
    temp = [0 for i in range(n)]
    while size < n:
        merge_pass(arr, temp, size, n)
        size = size * 2

    return arr


def merge_pass(arr, temp, size, n):
    lo1 = 0
    while lo1 + size < n + 1:
        hi1 = lo1 + size - 1
        lo2 = lo1 + size
        hi2 = lo2 + size - 1

        if hi2 >= n:
            hi2 = n - 1

        merge2(arr, temp, lo1, hi1, lo2, hi2)
        lo1 = hi2 + 1

    copy(arr, temp, n)


def merge2(arr, temp, lo1, hi1, lo2, hi2):
    i = lo1
    j = lo2
    k = lo1

    while i <= hi1 and j <= hi2:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1

    while i <= hi1:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= hi2:
        temp[k] = arr[j]
        j += 1
        k += 1

    print("size({0}): {1}".format((hi1-lo1+1), temp))


def copy(arr, temp, n):
    for i in range(n):
        arr[i] = temp[i]


if __name__ == "__main__":
    a = [15, 14, 32, 12, 18, 39, 21, 25, 8, 6, 3]
    print('initial :', a)
    print('--------------------------------------------------')
    a2 = merge_sort_bu(a)
    print('--------------------------------------------------')
    print('sorted :', a2)
