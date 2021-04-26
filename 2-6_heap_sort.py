import heapq

def adjust(arr, root_idx, max_idx):

    while 2 * root_idx + 1 <= max_idx: # 자식 노드가 마지막 인덱스 보다 작을 때 까지
        child_idx = 2 * root_idx + 1 # 자식 노드 설정
        print("root:", root_idx,  "value:", arr[root_idx])
        print("child:", child_idx, "value:", arr[child_idx])
        print("size:", 2 * root_idx + 1, "/",max_idx)
        if child_idx < max_idx and arr[child_idx] < arr[child_idx+1]: # 자식노드끼리 비교해서 둘 중 큰거를 부모노드와 비교
            child_idx += 1
            print("형제가 더 큼, child idx:", child_idx, "value:", arr[child_idx])

        if arr[root_idx] >= arr[child_idx]: # 부모와 자식 노드 비교
            print("부모가 더 큼, while 탈출") # 부모가 더 크면 힙 유지
            break
        else:
            arr[root_idx], arr[child_idx] = arr[child_idx], arr[root_idx] # 자식이 더 크면 부모와 자식을 바꿈
            print("부모와 더 큰 자식을 교체합니다. :", arr[root_idx], arr[child_idx])
            root_idx = child_idx # 부모가 아래로 내려와 힙이 깨졌으므로 자식 노드와 비교해줘야함
            print("자식 노드를 루트로 설정합니다.", root_idx,"value:", arr[root_idx])
            print(arr)
    print("**********while완료**********")

    return arr

def heap_sort(arr):
    max_idx = len(arr)  #인덱스가 0부터 시작하기 때문

    #힙만들기
    for i in range(max_idx//2 + 1, 0, -1): # max_idx//2 은 가장 마지막 부모 노드의 인덱스
        adjust(arr, i, max_idx)
    print(arr)
    print("++++++++++++++++++++++")
    #가장 큰 수 빼와서 힙 유지하기
    for i in range(len(arr)):
        arr[0], arr[max_idx] = arr[max_idx], arr[0] #가장 큰 수와 마지막 요소 위치 변경하여 가장 큰수 pop
        max_idx -= 1 # 가장 큰 수가 빠졌으므로 인덱스 조정
        adjust(arr, 0, max_idx) # 힙이 깨졌으므로 재정비

        print(arr)
    print("______________________________")
    return arr #결과 반환

def heap_sort_descending(arr):
    result = []
    max_idx = len(arr) - 1
    #힙만들기
    for i in reversed(range(0, max_idx//2 + 1)): #i는 각 부모노드의 역순 #hsize는 힙의 마지막 인덱스
        adjust(arr,i, max_idx)
    print("\n++++++++++++++++초기화 완료++++++++++++++++")
    print(arr)
    print("++++++++++++++++초기화 완료++++++++++++++++\n")
    #가장 큰 수 빼와서 힙 유지하기

    for i in range(len(arr)):
        arr[0], arr[max_idx] = arr[max_idx], arr[0]
        result.append(arr[max_idx])
        adjust(arr, 0, max_idx-1)
        max_idx -= 1
        print(arr)
    print("______________________________")
    return result


#arr = [8, 1, 3, 4, 10, 2,9]
arr = [26,5,77,1,61,11,59,15,48,19,29]
print(heap_sort_descending(arr))
