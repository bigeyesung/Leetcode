'''
Find the index i of the next maximum number x.
Reverse i + 1 numbers, so that the x will be at A[0]
Reverse x numbers, so that x will be at A[x - 1].
Repeat this process N times.
'''
class Solution:    
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            tmp1 = A[:i:-1]
            tmp2 = A[:i]
            tmp1.extend(tmp2)
            A = tmp1
            # A = A[:i:-1] + A[:i]
            print(A)
        return res
a = [4,1,5,3]
tmp = a[:1:-1]
sol = Solution()
ret = sol.pancakeSort([3,2,4,1])
print(ret)