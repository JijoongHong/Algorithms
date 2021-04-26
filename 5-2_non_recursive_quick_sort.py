class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def top(self):
        return len(self.items)

    def isEmpty(self):
        return self.items.__len__() == 0



def quick_sort2(arr, lo, hi):
    size = hi - lo + 1
    stack = [0 for i in range(size)]
    top = -1

    top += 1
    stack.append(lo)
    top += 1
    stack.append(hi)

    while top >= 0:

        hi = stack.pop()
        top -= 1
        lo = stack.pop()
        top -= 1

        pivot = partition(arr, lo, hi)

        if pivot -1 > lo:
            top += 1
            stack.append(lo)
            top += 1
            stack.append(pivot -1)

        if pivot+1 < hi:
            top += 1
            stack.append(pivot + 1)
            top += 1
            stack.append(hi)

def partition2(arr, lo, hi):
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] <= arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    print(arr)
    return i+1

def quick_sort(arr, lo, hi):
    stack = Stack()

    stack.push(lo)
    stack.push(hi)

    while stack.isEmpty() != True:

        hi = stack.pop()
        lo = stack.pop()

        pivot = partition(arr, lo, hi)

        if pivot-1 > lo:
            stack.push(lo)
            stack.push(pivot -1)

        if pivot+1 < hi:
            stack.push(pivot + 1)
            stack.push(hi)

def partition(arr, pivot, hi):

    i = pivot + 1
    j = hi
    while True:
        while i < hi and arr[i] < arr[pivot]:
            i += 1
        while j > pivot and arr[j] > arr[pivot]:
            j -= 1
        if j <= i:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[pivot], arr[j] = arr[j], arr[pivot]
    print(arr[j], j)
    return j


if __name__ == "__main__" :
    a = [4,2,8,5,3,9,7,40, 23, 42, 34, 53, 32, 22, 34, 53,0]
    #a = [3,2,4,5,8]
    print("\n")
    quick_sort(a, 0, len(a)-1)
    print("result is", a)


'''
ef quick_sort2(arr, lo, hi):
    size = hi - lo + 1
    stack = [0 for i in range(size)]
    top = -1

    top += 1
    stack.append(lo)
    top += 1
    stack.append(hi)

    while top >= 0:

        hi = stack.pop()
        top -= 1
        lo = stack.pop()
        top -= 1

        pivot = partition(arr, lo, hi)

        if pivot -1 > lo:
            top += 1
            stack.append(lo)
            top += 1
            stack.append(pivot -1)

        if pivot+1 < hi:
            top += 1
            stack.append(pivot + 1)
            top += 1
            stack.append(hi)

def partition2(arr, lo, hi):
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] <= arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1


'''