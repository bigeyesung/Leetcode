import bisect
class Solution:
    def increasingTriplet(self, nums):
        # keep track of the smallest 1st and 2nd element in triplet
        # if there exist a 3rd element, return True.
        l, r = float('inf'), float('inf')
              
        for n in nums:
            if n == l or n == r:
                continue
            if n < l:
                l = n
            elif n < r:
                r = n
            else:
                return True
        return False

    def increasingTriplet1(self, nums):
        inc = [float('inf')] * 2
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= 2:
                return True
            inc[i] = x
        return False

if __name__ == "__main__":
    sol = Solution()
    arr = [1,8,3,5,7]
    ret = sol.increasingTriplet1(arr)
    print(ret)