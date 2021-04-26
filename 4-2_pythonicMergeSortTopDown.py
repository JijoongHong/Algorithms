def merge_sort_td(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort_td(arr[:mid])
    right = merge_sort_td(arr[mid:])

    return merge(left, right)


def merge(left, right):
    # if not left or not right: #둘 중 하나가 비었으면 / 둘 다 비었으면
    #    return left or right  #비지 않은 것 출력 / 빈 것 출력
    result = []
    i, j = 0, 0

    # 인덱스 증가시키며 큰 값 집어넣기
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 항목 다 집어넣기
    if left[i:]:
        result.extend(left[i:])

    if right[j:]:
        result.extend(right[j:])

    return result


if __name__ == "__main__":
    a = [15, 14, 32, 12, 18, 39, 21, 25, 8, 6, 3]
    print('initial :', a)
    print('--------------------------------------------------')
    a2 = merge_sort_td(a)
    print('--------------------------------------------------')
    print('sorted :', a2)