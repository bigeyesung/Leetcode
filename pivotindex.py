def pivotIndex(nums):
    rightsum, leftsum = sum(nums),0
    for ind in range(len(nums)):
        rightsum -= nums[ind]
        if rightsum == leftsum:
            return ind
        leftsum += nums[ind]
    return -1


arr = [1,7,3,6,5,6]
ret = pivotIndex(arr)
