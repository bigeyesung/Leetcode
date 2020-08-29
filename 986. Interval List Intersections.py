class Solution:
    # two for-loops iteration
    # save anserts to set

    def intervalIntersection(self, A, B):
        tmp = []
        for ind1 in range(len(A)):
            for ind2 in range(len(B)):
                # check B ele start <= A end: intervals
                if B[ind2][0]<=A[ind1][1] and B[ind2][1]>=A[ind1][0]:
                    left = max(B[ind2][0], A[ind1][0])
                    right = min(B[ind2][1],A[ind1][1])
                    tmp.append([left,right])

        return tmp
def intervalIntersection1(self, A, B):   
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            l, r = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            if l <= r:
                ans.append([l, r])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1    
        return ans
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
sol = Solution()
res = sol.intervalIntersection(A,B)
print(res)