
def maxCoins(nums):
    def recursive(i, j):
        if i >= j - 1:
            return 0
        if (i, j) in dp:
            return dp[(i, j)]
        tmp = 0
        for k in range(i + 1, j):
            last_burn = nums[i] * nums[k] * nums[j]
            tmp = max(tmp, recursive(i, k) + recursive(k, j) + last_burn)
        dp[(i, j)] = tmp
        return dp[(i, j)]
    
    nums = [1] + [x for x in nums if x > 0] + [1]
    dp = {}
    return recursive(0, len(nums) - 1)

arr = [2,4]
res = maxCoins(arr)
print(res)
