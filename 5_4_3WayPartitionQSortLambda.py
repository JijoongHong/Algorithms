def qsort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    lower = list(filter(lambda x : x < pivot, a))
    equal = list(filter(lambda x : x == pivot, a))
    higher = list(filter(lambda x : x > pivot, a))

    print("pivot:", pivot, "| lower:", lower, "| equal", equal, "| higher:", higher)
    print(">>> current state", lower+equal+higher)
    print("------------------------------------------------------------------------")
    return qsort(lower) + equal + qsort(higher)


if __name__ == "__main__" :
    a = [40, 23, 42, 34, 53, 32, 22, 34, 53]
    print("\n")
    b = qsort(a)
    print(b)