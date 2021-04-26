def quick_sort(arr, lo, hi):
    if lo >= hi:
        return

    pivot = partition(arr, lo, hi)
    quick_sort(arr, lo, pivot-1)
    quick_sort(arr, pivot+1, hi)


def partition(arr, pivot, hi):
    i = pivot + 1
    j = hi
    while True:
        while i < hi and arr[i] < arr[pivot]: #피봇보다 큰거 찾을 때 까지
            i += 1
        while j > pivot and arr[j] > arr[pivot]: #피봇보다 작은거 찾을 때 까지
            j -= 1
        if j <= i: #크로스 되면 종료
            break
        arr[i], arr[j] = arr[j], arr[i] #큰값과 작은값 위치 변경
        i += 1 #각자 다음 인덱스로
        j -= 1

    arr[pivot], arr[j] = arr[j], arr[pivot] #피봇과 j위치 변경

    return j #피봇은 j

if __name__ == "__main__" :
    a = [4,1,2,9,3,7]
    print("\n")
    quick_sort(a, 0, 5)
    print("result is", a)