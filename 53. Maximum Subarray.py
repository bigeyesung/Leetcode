class Solution():
# idea is to find the largest subarry that the sum is >=0
# Also, make sure compare new sum with the old sum 
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far, curr_sum = -2**31, 0
        for i in range(len(nums)):
            if curr_sum+nums[i] < 0:
                curr_sum, max_so_far = 0, max(max_so_far, nums[i])
            else:
                curr_sum, max_so_far = curr_sum + nums[i], max(max_so_far, curr_sum + nums[i])
        return max_so_far

    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far, curr_sum = max(nums), 0
        for i in range(len(nums)):
            if curr_sum+nums[i] < 0:
                curr_sum = 0
            else:
                curr_sum, max_so_far = curr_sum + nums[i], max(max_so_far, curr_sum + nums[i])
        return max_so_far

    def test(self,nums):
        max_so_far, cur_sum = max(nums), 0
        for num in nums:
            if cur_sum+num>=0:
                cur_sum, max_so_far = cur_sum+num, max(max_so_far, cur_sum+num)
            else:
                cur_sum = 0
        return max_so_far

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ret = sol.maxSubArray1(nums)
    print(ret)