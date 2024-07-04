class Solution:
    def threeSum(self, nums):
        ans = []
        if len(nums)<3:
            return ans
        #a+b+c=0->b+c = -a
        
        #repeat input/output
        #cornor case
        #test case
        #sudo code
        #
        #code
        
        #sort first
        nums.sort()
        
        for ind in range(0,len(nums)-2):
            target = -nums[ind]
            upper = len(nums)-1
            lower = ind+1
            # we don't use the same duplicate target number
            if ind and nums[ind-1] == nums[ind]:
                continue
                
            while(lower < upper):
                sums = nums[lower]+ nums[upper]
                #bigger
                if sums>target:
                    upper = upper -1
                #smaller
                elif sums<target:
                    lower = lower +1
                #equal
                else:
                    tmp = [nums[ind], nums[lower], nums[upper]]
                    ans.append(tmp)
                    while True:
                        lower = lower +1
                        judge1 = lower < upper
                        # make sure no duplicated lower number
                        judge2 = nums[lower-1] == nums[lower]
                        if judge1== False or judge2 == False:
                            break
                        
        return ans