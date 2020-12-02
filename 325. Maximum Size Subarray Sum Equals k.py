# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:

# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# Follow Up:
# Can you do it in O(n) time?

def func(nums, k):
    SUM=0
    res=0
    table = {}
    for ind in range(len(nums)):
        SUM+=nums[ind]
        if SUM==k:
            res=ind+1
        elif table.get(SUM-k):
            res=max(res,ind-table[SUM-k])
        if table.get(SUM)==None:
            table[SUM]=ind
    return res

if __name__ == "__main__":
    nums = [1, -1, 5, -2, 3]
    k = 3
    ret = func(nums, k)
    print(ret)
        