import collections
class Solution:
    def commonChars(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())   

if __name__ == "__main__":
    sol=Solution()
    arr = ["bella","label","roller"]
    ret = sol.commonChars(arr) 