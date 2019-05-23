import random

# find the kth smallest element in array a with size of n by using Randomized-select in CLRS
def randomized_select(a, n, k) :
    return randomized_select_helper(a, 0, n-1, k+1)

# find the kth smallest element in array a with size of n by using the worst-case linear-time algorithm in CLRS
def deterministic_select(a, n, k) :
    if (n == 1) :
        return a[0]
    medians = find_medians(a, n)
    median = deterministic_select(medians, len(medians), (len(medians)-1)//2)
    exchange(a, n-1, a.index(median))
    q = partition(a, 0, n-1)
    if (k == q) :
        return a[q]
    elif (k < q) :
        return deterministic_select(a[:q], q, k)
    else :
        return deterministic_select(a[q+1:], n-q-1, k-q-1)

# check whether the kth smallest element in array a with size of n is the ans
def checker(a, n, k, ans) :
    less = 0
    for element in a :
        if (element < ans) :
            less = less + 1
    return (less == k)



# helper function of randomized_select function, for recursion
def randomized_select_helper(a, p, r, i) :
    if (p == r) :
        return a[p]
    q = randomized_partition(a, p, r)
    k = q - p + 1
    if (i == k) :
        return a[q]
    elif (i < k) :
        return randomized_select_helper(a, p, q-1, i)
    else :
        return randomized_select_helper(a, q+1, r, i-k)

# modified version of partition function, which selects pivot randomly, not just a[r]
def randomized_partition(a, p, r) :
    i = random.randint(p, r)    # select a number(= pivot) randomly
    exchange(a, r, i)           # move the pivot to the right end
    return partition(a, p, r)   # partition

# partition the array a[p:r+1] into two parts, where one is less than a[r] and another is greater than a[r]
def partition(a, p, r) :
    x = a[r]
    i = p-1
    for j in range(p, r) :
        if (a[j] <= x) :
            i = i+1
            exchange(a, i, j)
    exchange(a, i+1, r)
    return i+1

# exchange a[x] and a[y]
def exchange(a, x, y) :
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

# divide the array a with size of n into groups of 5 elements (if n % 5 != 0, size of one group is less than 5)
# find median in each group by insertion sort, and return the list of medians
def find_medians(a, n) :
    group_number = n // 5
    remaining = n % 5
    result = []
    for i in range(1, group_number+1) :
        median = find_median(a[(i-1)*5:i*5], 5)
        result.append(median)
    if (remaining != 0) :
        median = find_median(a[group_number*5:], remaining)
        result.append(median)
    return result

# find a (lower) median in array a with size of n by using insertion sort
def find_median(a, n) :
    a = insertion_sort(a, n)
    return a[(n-1) // 2]

# sort the array a with size of n by using insertion sort
def insertion_sort(a, n) :
    for j in range(1, n) :
        key = a[j]
        i = j-1
        while (i>=0 and a[i]>key) :
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a
