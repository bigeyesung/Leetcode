def missingElement(nums, k):
    pre = nums[0]
    for ind in range(1,len(nums)):
        if (nums[ind] - pre - 1)>k:
            return pre + k
        else:
            k -= nums[ind] - pre -1
        pre = nums[i]
    return pre + k