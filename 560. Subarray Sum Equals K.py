class Solution:
    def subarraySum(self, nums, k):
        #the idea is curSum=nums[0]+....+nums[i]
        #if j<i, nums[0]+....+nums[j]=curSum-k. there must exists that nums[j+1]+....nums[i]==k
        #that is to say if we want to find curSum=k, just check if curSum-k exists or not

        #curSum=0, that is to say the opposite is nums[0]+.....+nums[n-1] : the whole array must exist
        sumTable = {}
        sumTable[0] = 1
        res = 0
        curSum = 0
        for num in nums:
            curSum += num
            #is it like two sum question.
            if sumTable.get(curSum-k) != None:
                res += sumTable[curSum-k]

            if sumTable.get(curSum) == None:
                sumTable[curSum] = 1
            else:
                sumTable[curSum] += 1
        return res
    #brute-force
    def subarraySum1(self, nums, k):
        #create sum table
        #length is n+1 is due to we need add 0 
        n=len(nums)
        sumArr=[0]*(n+1)
        for ind in range(1,n+1):
            sumArr[ind]=sumArr[ind-1]+nums[ind-1]
        
        #find all pairs
        #ind1+1 is the offset as total longth for sumArr is n+1
        count=0
        for ind in range(len(nums)):
            for ind1 in range(ind,len(nums)):
                if sumArr[ind1+1]-sumArr[ind]==k:
                    count+=1
        return count



if __name__ == "__main__":
    nums = [1,2,3]
    k = 3
    sol=Solution()
    ret=sol.subarraySum(nums,k)
    print(ret)