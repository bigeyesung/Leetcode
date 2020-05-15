def maxSubArrayLen(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    sums = {}
    cur_sum, max_len = 0, 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum == k:
            max_len = i + 1
        elif cur_sum - k in sums:
            max_len = max(max_len, i - sums[cur_sum - k])
        if cur_sum not in sums:
            sums[cur_sum] = i  # Only keep the smallest index.
    return max_len


nums = [1, -1, 5, -2, 3] 
k = 3

ret = maxSubArrayLen(nums,k)
print(ret)