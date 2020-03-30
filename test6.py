def myfunc(ele):
    return ele[1]

def nth_most_rare(elements, n):
    """
    :param elements: (list) List of integers.
    :param n: (int) The n-th element function should return.
    :returns: (int) The n-th most rare element in the elements list.
    """
    import collections
    count = collections.Counter(elements)
    arr = []
    for key in count:
        tmp = [key,count[key]]
        arr.append(tmp)

    arr.sort(key = myfunc)
    return arr[n-1][0]



print(nth_most_rare([5, 4, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))