# 1. Show how many array access are in Mergesort- Merge**

## 1) 소스코드
'''
def mergeSortTD(arr, lo, hi):
      if lo == hi:
          return arr

      mid = (lo + hi) // 2
      merge\_sort\_td(arr, lo, mid)
      merge\_sort\_td(arr, mid+1, hi)
      merge(arr, lo, mid, hi)

      return arr



def merge(arr, lo, mid, hi):

      temp = []
      i = lo
      j = mid + 1
      
      while i <= mid and j <= hi: 	# 인덱스 증가시키며 큰 값 집어넣기
          if arr[i] <= arr[j]: 		##############(1) : 2 reads
              temp.append(arr[i]) 	##############(2) : 1 read, 1write
              i += 1
          else:
          temp.append(arr[j])
          j += 1

      if I > mid: 			# 남은 항목 다 집어넣기
          temp.extend(arr[j:hi+1])
      else:
          temp.extend(arr[i:mid+1])

      for i in range(len(temp)): 		# 원본 리스트로 옮기기
          arr[lo+i] = temp[i]		##############(3) : 1 read, 1write
'''

## 2) 설명

- 두 배열을 병합하는 과정은 각 배열의 값을 비교하고, 그 중 더 작은 값을 추가하는 방식으로 이루어진다. 
- 그러므로 arr배열에서 i, j 인덱스의 값을 불러오는 과정에서 (1) 2번의 read가 발생한다. 
- 비교를 마친 이후, (2) arr의 값을 읽어오는 1번의 read, temp 배열에 큰 값을 추가할 때 1번의 write 가 발생한다. 
- temp에 병합이 완료된 데이터가 전부 저장이 되었다면, 이 값을 원본의 arr 리스트에 복사하는 작업을 한다. 이 과정에서 (3) temp의 값을 읽는 read가 1회, 이를 arr에 쓰는 write가 1회 발생한다.
- 이러한 작업은 특정 크기의 작은 배열들이 병합될 때 N회 일어나게 된다. 즉 원본의 4개 배열이 있을 때 1 -> 2 개씩 병합하게 되고, 각 단계마다 모든 원본 배열의 항목에 접근하게 된다.  
- 그러므로 merge 과정은 4N read, 2N write가 일어나며 이를 합산 시 array access 횟수는 6N회라고 볼 수 있다. 


# 2. Write your own merge sort algorithm in bottom-up approach, and  describe in detail of yours** 

## 1) 개요

- bottom-up 접근 방식의 merge sort는 하나의 배열을 반으로 분할하는 과정을 1개의 요소가 남을 때 까지 반복한 후 이를 정렬 및 병합하는 top-down 방식과 달리 분리되어있는 요소를 병합해가며 정렬하는 방법이다.

## 2) mergeSortBU( )

'''
def mergeSortBU(arr):
`    `size = 1
`    `n = len(arr)
`    `while size < n:
`        `getIdx(arr, size, n)
`        `size = size \* 2

`    `return arr

'''

- 요소들이 각기 분리되었다고 가정하므로 초기 size는 1이 되며, 이 size는 해당사이즈에 대한 병합과 정렬이 끝났을 때 2배씩 증가한다. 
- 병합과 정렬을 위해서는 접근해야하는 인덱스를 알아야 한다. 그러므로 getIdx함수를 호출한다. 이후 getIdx는 인덱스 정보로 merge 함수를 호출한다. 
- 이러한 과정을 size가 데이터의 개수를 의미하는 n에 다다를 때 까지 반복한다. 






## 3) getIdx( ), merge( )
'''
def getIdx(arr, size, n):
`    `lo1 = 0
`    `while lo1 + size < n + 1:
`        `hi1 = lo1 + size - 1
`        `lo2 = lo1 + size
`        `hi2 = lo2 + size - 1

`        `if hi2 >= n:
`            `hi2 = n - 1

`        `merge(arr, lo1, hi1, lo2, hi2)
`        `lo1 = hi2 + 1

'''

- getIdx에서는 각 사이즈별로 병합 및 정렬할 두 작은 배열의 시작과 끝 위치를 지정해준다. 
- 이를 바탕으로 인덱스를 지정하여, merge 함수를 호출한다.
- 이 과정을 원본 배열의 처음부터 마지막 요소까지 반복한다.
- 만약 두번째 배열의 인덱스가 n을 초과한다면 가장 끝 인덱스로 맞춰주는 작업을 수행한다.
'''
def merge(arr, lo1, hi1, lo2, hi2):
`    `i = lo1
`    `j = lo2
`    `temp = []

`    `while i <= hi1 and j <= hi2:
`        `if arr[i] <= arr[j]:
`            `temp.append(arr[i])
`            `i += 1

`        `else:
`            `temp.append(arr[j])
`            `j += 1

`    `while i <= hi1:
`        `temp.append(arr[i])
`        `i += 1

`    `while j <= hi2:
`        `temp.append(arr[j])
`        `j += 1

`    `for i in range(len(temp)):
`        `arr[lo1+i] = temp[i]

`    `print("size({0}) | merged data : {1} | current state : {2}".format((hi1-lo1+1), temp, arr))
'''

- 두 작은 배열의 시작과 끝을 입력받은 merge 함수는 각 배열의 값을 비교하고, 그 중 더 작은 값을 temp 리스트에 추가한다. 
- 만약 비교를 마쳤을 시 미처 비교되지 않은 요소가 있다면 이를 추가한다.
- 병합과 정렬이 완성된 temp 함수를 원본 배열 arr에 저장한다. 


## 4) 예시


<img width="801" alt="스크린샷 2021-04-29 오전 1 21 23" src="https://user-images.githubusercontent.com/63644587/116438222-36e69880-a889-11eb-8f3b-46962eab4968.png">



- 18, 13, 4, 3 으로 이루어진 임의의 배열이 있다고 가정하자.
- 맨 처음 시행에서는 각 배열에 low와 high를 지정해준다. (단 이 때 size가 1이므로 low와 high 위치는 같다.) 이 작업은 getIdx 함수가 수행한다.
- getIdx( )가 인덱스를 지정 후 merge( )함수를 호출하여 병합 및 정렬 작업을 수행한다.
- 위 작업을 전체 배열에 대해 병합 및 정렬이 끝날 때 까지 반복한다.
- 이후  mergeSortBU( )함수로 되돌아가 size를 조정하고 위에 언급한 인덱스 지정, 병합 및 정렬 작업을 반복한다. 

## 5) 실행 결과

![image](https://user-images.githubusercontent.com/63644587/116438271-40700080-a889-11eb-9f76-ffb366817eaf.png)


- 실행 결과 size 별로 순차적인 정렬 및 병합을 수행하는 것을 알 수 있다.
