# kth smallest ele in a sorted matrix
import heapq
def kthSmallest( matrix, k):
    heap, res = [(row[0], r, 0) 
                for r, row in enumerate(matrix) 
                if row], 0
    heapq.heapify(heap)
    for k in range(1, k + 1):
        res, row, col = heapq.heappop(heap)
        if col + 1 < len(matrix[row]):
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
    return res

def kthSmallest2( matrix, k):
    heap, res, n = [(matrix[0][0], 0, 0)], 0, len(matrix)
    for k in range(1, k + 1):
        res, row, col = heapq.heappop(heap)
        if not row and col < n - 1:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        if row < n - 1:
            heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
    return res

matrix = [[1,2],[1,3]]
k = 2
res = kthSmallest2( matrix, k)
print(res)