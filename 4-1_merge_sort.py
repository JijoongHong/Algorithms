def merge_sort_td(arr, lo, hi):
    if lo == hi:
        return arr

    mid = (lo + hi) // 2
    merge_sort_td(arr, lo, mid)
    merge_sort_td(arr, mid+1, hi)
    merge(arr, lo, mid, hi)

    return arr


def merge(arr, lo, mid, hi):

    temp = []
    i = lo
    j = mid + 1

    # 인덱스 증가시키며 큰 값 집어넣기
    while i <= mid and j <= hi:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # 남은 항목 다 집어넣기
    if i > mid:
        temp.extend(arr[j:hi+1])
    else:
        temp.extend(arr[i:mid+1])

    # 원본 리스트로 옮기기
    for i in range(len(temp)):
        arr[lo+i] = temp[i]

    # 진행상황 확인
    print("merged data : {0} | current state : {1}".format(temp, arr))


if __name__ == "__main__":
    a = [15, 14, 32, 12, 18, 39, 21, 25, 8, 6, 3]
    print('initial :', a)
    print('--------------------------------------------------')
    a2 = merge_sort_td(a, 0, len(a)-1)
    print('--------------------------------------------------')
    print('sorted :', a2)