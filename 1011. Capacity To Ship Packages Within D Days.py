class Solution:
    def shipWithinDays(self, weights, D):
        def search(nums, targetWeight):
            shipDay = 1
            curWeight = 0
            for num in nums:
                curWeight += num
                if curWeight > targetWeight:
                    #reset curWeight
                    curWeight = num
                    shipDay += 1
            return shipDay
        
        minCapacity = max(weights)
        maxCapacity = sum(weights)
        
        while minCapacity <= maxCapacity:
            midCapacity = (minCapacity + maxCapacity) // 2
            shipDay = search(weights, midCapacity)
            # It means we need bigger capacity for each day
            if shipDay > D:
                minCapacity = midCapacity + 1
            # It means we need to decrease capacity for each day
            else:
                maxCapacity = midCapacity - 1
                
        return minCapacity


if __name__ == "__main__":
    sol=Solution()
    weights = [3,2,2,4,1,4]
    D = 3
    sol.shipWithinDays(weights,D)