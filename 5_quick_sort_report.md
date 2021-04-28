**HW2\_20176963 홍지중**

**Problem 1**
**suppose we implement QuickSort so that ChoosePivot always selects the "first element" of the array. What is the running time of this algorithm on an input array that is already sorted?**

This is the worst case and its running time is O(n2 ).

Suppose we have an array 1~5. 

|1|2|3|4|5|->|1|2|3|4|5|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|`  `i||||j||`  `j|i||||
In this case pivot is 1 and increment i until find element which is bigger than pivot. So i will stop at second index since array is already sorted. And j will be decremented until find element which is smaller than pivot. But there is no smaller element, so j will stop at first index, which is pivot. So now the first element is sorted and in this level, there are five comparisons. Once partitioning has done, we keep sort the rest of element. Now i begin to increment from index 2 and j will stop at index 2. This level makes four comparisons. In this manner, the total running time is 5+4+3+2+1 = 15.

we can generalize this case using tree. 

` `![](Aspose.Words.23446be4-3e69-4d16-8e4a-fc1c70d60e8b.001.jpeg)

So running time of array which has n elements is Tn=Tn-1+ Θn=  n(n+1)2=  n2+n   2 , and big-O notation is O(n2 ).

**Problem 2
Suppose we run QuickSort on some input, and magically, every recursive all chooses the "median" element of its subarray as its pivot. What's the running time in this case?**

This is the best case since the array always divided by half. Its running time is nlogn. 

Suppose we have an array 1~7. 

|1|2|3|4|5|6|7|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
In this case pivot is 4, and already there are smaller elements are located in left side and bigger elements are located in right side. In this level, there are 7 comparisions. And recursively conduct quick sort on left and right side until each array has only one element. 

![텍스트, 시계이(가) 표시된 사진

자동 생성된 설명](Aspose.Words.23446be4-3e69-4d16-8e4a-fc1c70d60e8b.002.jpeg)

There are 2 times of division, that means it has 2 levels. Each level has approximately n comparisons, so running time is 7(n) \* 2(log7). 

we can generalize this case using tree. 

![](Aspose.Words.23446be4-3e69-4d16-8e4a-fc1c70d60e8b.003.jpeg)

The number of level(k) is n2k = 1, 2k = n, k=logn. And big-O notaition is (time per each level) \* (height) = n\*nlogn = O(nlogn). In this case every recursive call makes 2 subproblems with same size. So, running time is  Tn=Tn2+Tn2+ Θn 

**Problem 3
If T(n) = T(n/3) + T(2n/3) + n, express T(n) in big-O**

Expressing T(n) using recursive tree, result is following

![](Aspose.Words.23446be4-3e69-4d16-8e4a-fc1c70d60e8b.004.jpeg)

Every branch is divided until each array becomes size 1. And this is not a perfect binary tree since it is not divided by half.

Therefore, leftmost branch’s level(k) is n3k =1, 3k = 1, k = log3n. 

And rightmost branch’s level(l) is  n23l=1, l = log3/2n.

Therefore, lower bound will be height of leftmost × n = k × n=nlog3n  

and upper bound will be height of rightmost × n = l × n=nlog3/2n  

Since nlog3n  ≤Tn≤ nlog3/2n is true, big-O notation of Tn  is O(nlogn).

We can prove this with substitution method, which is the way of proving an asymptotic bound on a recurrence by induction. Assume that T(n) = O(nlogn ), T(N) should be smaller or equal than c\*nlogn, and c should be bigger than 0. That means Ogn=fn:n0≤n,0≤fn≤c\*gn 

Tn ≤Tn3+T2n3+n ≤dn3logn3+d2n3log2n3+n

`     `= dn3\*(log n-log3+2logn-2log3)+n

`     `= d n3\*(3log n-3log3+2)+n

`      `= d n3\*(3log n-3log3+2)+n

`      `= d\*nlogn-dn(log3-23  )+n

Therefore, 

Tn ≤dnlogn, as long as d ≥1/(log3-23  ), 

And big-O notation of Tn is O(nlogn)


**Problem 4
Implement 3-way partition.** 

def partition(a, lo, hi):*

`    `lt = lo
`    `i = lo 
`    `gt = hi 
`    `pivot = a[lo] 

`    `while i <= gt:
`        `if a[i] < pivot:
`            `a[lt], a[i] = a[i], a[lt]
`            `lt += 1
`            `i += 1
`        `elif a[i] > pivot:
`            `a[i], a[gt] = a[gt], a[i]
`            `gt -= 1
`        `else:
`            `i += 1

`    `return lt, gt


def quick\_sort(a, lo, hi):*
`    `if lo >= hi:
`        `return

`    `lt, gt = partition(a, lo, hi)

`    `quick\_sort(a, lo, lt - 1)
`    `quick\_sort(a, gt + 1, hi)


if \_\_name\_\_ == "\_\_main\_\_" :
`    `a = [40, 23, 42, 34, 53, 32, 22, 34, 53]
`    `quick\_sort(a, 0, 8)

This method set the lt(litte) and gt(greater) and compare pivot with every element in the array. If find the element which is smaller than pivot, this element is sent to “lt” boundary, and if find the element bigger than pivot, this element is sent to “gt” boundary, while let equal element stay at its position. Now array is divided into 3 small arrays which is lower than pivot, equal to pivot, and bigger than pivot. And recursivley conduct quick sort on lower and bigger array.  

The result is following. 

![텍스트이(가) 표시된 사진

자동 생성된 설명](Aspose.Words.23446be4-3e69-4d16-8e4a-fc1c70d60e8b.005.png)

There is another implementation of 3-way quick sort which uses small anonymous function, lambda. We can easily filter values in a given condition(smaller, equal, higher). After that, do some recursive tasks to lower and higher array, and finally every divided array is combined. 

def qsort(a):
`    `if len(a) <= 1:
`        `return a

`    `pivot = a[0]
`    `lower = list(filter(lambda x : x < pivot, a))
`    `equal = list(filter(lambda x : x == pivot, a))
`    `higher = list(filter(lambda x : x > pivot, a))


`    `return qsort(lower) + equal + qsort(higher)


if \_\_name\_\_ == "\_\_main\_\_" :
`    `a = [40, 23, 42, 34, 53, 32, 22, 34, 53]
`    `b = qsort(a)
`    `print(b)

The result is following. 

![텍스트이(가) 표시된 사진

자동 생성된 설명](Aspose.Words.23446be4-3e69-4d16-8e4a-fc1c70d60e8b.006.png)

Difference between this method and the previous one is that this method uses auxillary space but the other one uses index to compare and swap in a given array. So even if second one looks more simple and easy to implement, it has bigger space complexity.


