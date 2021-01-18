#nums = [1,3,5,4,7] -> [1,3,5]
#nums = [1,3,5,4,7,8,10,12,14]-> [8,10,12,14]
#input: array:empty array
#input: interger/float/positive/negative
#output: integer

#corner case: empty array
#corner case: [-1,-1]

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        #iterate nums:
        #   for each iteration: 
        #       if num>previous num-> add it to subarray
        #       if not->check the subarray is empty or not-> if not-> keep it in the subarrays
        subarrays = []
        if not nums:
            return 0
        if len(nums)==1:
            return 1
            
        subarray = [nums[0]]
        maxLength = 0
        for ind in range(1,len(nums)):
            if nums[ind]>subarray[-1]:
                subarray.append(nums[ind])
            else:
                if subarray:
                    subarrays.append(subarray)
                    maxLength=max(maxLength,len(subarray))
                subarray=[nums[ind]]
        if len(subarray)!=1:
            subarrays.append(subarray)
        return maxLength
