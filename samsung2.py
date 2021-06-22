import collections
import heapq
def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    # ret = 0
    # table = collections.Counter(sales)
    
    # iterate the sales, find the pair: book:sale times.
    # put it in the heap,
    # from the heap, pop n times, and return n-th id

    table = collections.Counter(sales)
    values=table.values()
    heap=table.most_common()
    print(type(heap))
    heapq.heapify(heap)
    n=n-1
    while(n!=0):
        tmp = heapq.heappop(heap)
        print("remove node: ", tmp)
        n-=1
    return heap[0][0]
    # arr.sort(key=lambda x:x[1])
    # while(n!=0):
    #     arr.pop(0)
    #     n-=1
    # if len(arr)!=0:
    #     return arr[0][0]
    # else:
    #     return 0




print(nth_lowest_selling([5,4,3,5,4,5], 1))
print(nth_lowest_selling([5, 5, 3, 2, 1, 5, 4, 3, 3, 5, 4, 3, 5, 4, 5], 3))