class Solution:
    def singleNonDuplicate(self, nums):
        #input: arrays min len=1
        #output: int: int
        
        #corner cases: [1],[2 2 1]
        
        size = len(nums)
        left, right = 0, size // 2
        while left < right:
            pair_index = left + ( right - left ) // 2
            print(2*pair_index)
            print(nums[2*pair_index])
            print(nums[2*pair_index+1])
            if nums[2*pair_index] != nums[2*pair_index+1]:
                # If current pair is mis-matched
                # then go left-half to find the first pair of mis-match
                right = pair_index
            
            else:
                # If current pair is with the same number appeared twice
                # then go right-half to find the first pair of mis-match
                left = pair_index + 1
        
        # when the while loop terminates, left = right = the first pair index of mis-match
        return nums[2*left]

if __name__ == "__main__":
    sol=Solution()
    nums = [1,1,2,3,3,4,4,8,8]
    ret=sol.singleNonDuplicate(nums)