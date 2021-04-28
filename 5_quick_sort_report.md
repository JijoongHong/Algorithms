# **Problem 1**
**suppose we implement QuickSort so that ChoosePivot always selects the "first element" of the array. What is the running time of this algorithm on an input array that is already sorted?**

This is the worst case and its running time is O(n^2 ).

Suppose we have an array 1~5. 

<img width="845" alt="스크린샷 2021-04-29 오전 1 29 36" src="https://user-images.githubusercontent.com/63644587/116439298-5cc06d00-a88a-11eb-8a39-db28ca0d2fa7.png">


In this case pivot is 1 and increment i until find element which is bigger than pivot. So i will stop at second index since array is already sorted. And j will be decremented until find element which is smaller than pivot. But there is no smaller element, so j will stop at first index, which is pivot. So now the first element is sorted and in this level, there are five comparisons. Once partitioning has done, we keep sort the rest of element. Now i begin to increment from index 2 and j will stop at index 2. This level makes four comparisons. In this manner, the total running time is 5+4+3+2+1 = 15.

we can generalize this case using tree. 

![image](https://user-images.githubusercontent.com/63644587/116439327-62b64e00-a88a-11eb-830d-12f05fe5f4f1.png)

So running time of array which has n elements is 

<img width="624" alt="스크린샷 2021-04-29 오전 1 40 25" src="https://user-images.githubusercontent.com/63644587/116440891-e02e8e00-a88b-11eb-9cf0-22367a47d6cb.png">


and big-O notation is 
<img width="99" alt="스크린샷 2021-04-29 오전 1 40 42" src="https://user-images.githubusercontent.com/63644587/116440928-eae92300-a88b-11eb-9dd2-c71262eb2371.png">
.

# **Problem 2**
**Suppose we run QuickSort on some input, and magically, every recursive all chooses the "median" element of its subarray as its pivot. What's the running time in this case?**

This is the best case since the array always divided by half. Its running time is nlogn. 

Suppose we have an array 1~7. 

|1|2|3|4|5|6|7|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |

In this case pivot is 4, and already there are smaller elements are located in left side and bigger elements are located in right side. In this level, there are 7 comparisions. And recursively conduct quick sort on left and right side until each array has only one element. 

![image](https://user-images.githubusercontent.com/63644587/116439393-75308780-a88a-11eb-8853-d0da1f948c47.png)


There are 2 times of division, that means it has 2 levels. Each level has approximately n comparisons, so running time is 7(n) \* 2(log7). 

we can generalize this case using tree. 

![image](https://user-images.githubusercontent.com/63644587/116439426-7eb9ef80-a88a-11eb-9c77-fd3f56451e68.png)

The number of level(k) is 

<img width="585" alt="스크린샷 2021-04-29 오전 1 43 41" src="https://user-images.githubusercontent.com/63644587/116441354-57642200-a88c-11eb-8745-0f97f8f4d185.png">

And big-O notaition is (time per each level) \* (height) = n\*nlogn = O(nlogn). In this case every recursive call makes 2 subproblems with same size. So, running time is 

<img width="655" alt="스크린샷 2021-04-29 오전 1 44 49" src="https://user-images.githubusercontent.com/63644587/116441529-7cf12b80-a88c-11eb-8435-d90297092bf5.png">


# **Problem 3**
**If T(n) = T(n/3) + T(2n/3) + n, express T(n) in big-O**

Expressing T(n) using recursive tree, result is following

![image](https://user-images.githubusercontent.com/63644587/116439497-95f8dd00-a88a-11eb-9608-e321deb023fb.png)


Every branch is divided until each array becomes size 1. And this is not a perfect binary tree since it is not divided by half.

Therefore, leftmost branch’s level(k) is 

<img width="581" alt="스크린샷 2021-04-29 오전 1 46 50" src="https://user-images.githubusercontent.com/63644587/116441827-c5a8e480-a88c-11eb-8aed-0586ba4cb76d.png">


And rightmost branch’s level(l) is 

<img width="485" alt="스크린샷 2021-04-29 오전 1 48 05" src="https://user-images.githubusercontent.com/63644587/116441983-f4bf5600-a88c-11eb-807e-b61411d3fc36.png">


Therefore, lower bound will be height of leftmost × n = k × n=nlog3n  

and upper bound will be height of rightmost × n = l × n=nlog3/2n  

Since nlog3n  ≤T(n)≤ nlog3/2n
 is true, big-O notation of Tn  is O(nlogn).

We can prove this with substitution method, which is the way of proving an asymptotic bound on a recurrence by induction. Assume that T(n) = O(nlogn ), T(N) should be smaller or equal than c\*nlogn, and c should be bigger than 0. That means 

<img width="960" alt="스크린샷 2021-04-29 오전 1 49 44" src="https://user-images.githubusercontent.com/63644587/116442191-2cc69900-a88d-11eb-86cd-c4bd1df9a0b4.png">

<img width="834" alt="스크린샷 2021-04-29 오전 1 50 30" src="https://user-images.githubusercontent.com/63644587/116442284-4831a400-a88d-11eb-8dad-b1c3b2648dfd.png">


Therefore, 

<img width="294" alt="스크린샷 2021-04-29 오전 1 51 17" src="https://user-images.githubusercontent.com/63644587/116442370-64cddc00-a88d-11eb-9ce4-5b36a94fb9cb.png"> **when** 

<img width="328" alt="스크린샷 2021-04-29 오전 1 51 50" src="https://user-images.githubusercontent.com/63644587/116442447-78794280-a88d-11eb-97dd-b46cd83cbfc3.png">
 

And big-O notation of Tn is O(nlogn)


# **Problem 4**
**Implement 3-way partition quick sort.** 

    def partition(a, lo, hi):

          lt = lo
          i = lo 
          gt = hi 
          pivot = a[lo] 

          while i <= gt:
              if a[i] < pivot:
                  a[lt], a[i] = a[i], a[lt]
                  lt += 1
                  i += 1
              elif a[i] > pivot:
                  a[i], a[gt] = a[gt], a[i]
                  gt -= 1
              else:
                  i += 1

          return lt, gt


    def quick_sort(a, lo, hi):*
          if lo >= hi:
              return

          lt, gt = partition(a, lo, hi)

          quick_sort(a, lo, lt - 1)
          quick_sort(a, gt + 1, hi)


    if __name__ == "__main__" :
          a = [40, 23, 42, 34, 53, 32, 22, 34, 53]
          quick\_sort(a, 0, 8)

This method set the lt(litte) and gt(greater) and compare pivot with every element in the array. If find the element which is smaller than pivot, this element is sent to “lt” boundary, and if find the element bigger than pivot, this element is sent to “gt” boundary, while let equal element stay at its position. Now array is divided into 3 small arrays which is lower than pivot, equal to pivot, and bigger than pivot. And recursivley conduct quick sort on lower and bigger array.  

The result is following. 

![image](https://user-images.githubusercontent.com/63644587/116439584-ad37ca80-a88a-11eb-9a1b-6d7afd4867f0.png)


There is another implementation of 3-way quick sort which uses small anonymous function, lambda. We can easily filter values in a given condition(smaller, equal, higher). After that, do some recursive tasks to lower and higher array, and finally every divided array is combined. 

    def qsort(a):
          if len(a) <= 1:
              return a

          pivot = a[0]
          lower = list(filter(lambda x : x < pivot, a))
          equal = list(filter(lambda x : x == pivot, a))
          higher = list(filter(lambda x : x > pivot, a))


          return qsort(lower) + equal + qsort(higher)


    if __name__ == "__main__" :
          a = [40, 23, 42, 34, 53, 32, 22, 34, 53]
          b = qsort(a)
          print(b)

The result is following. 

![image](https://user-images.githubusercontent.com/63644587/116439602-b32dab80-a88a-11eb-97f4-c55c41856913.png)

Difference between this method and the previous one is that this method uses auxillary space but the other one uses index to compare and swap in a given array. So even if second one looks more simple and easy to implement, it has bigger space complexity.


