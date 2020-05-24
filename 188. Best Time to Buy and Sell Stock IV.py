class Solution:
    def maxProfit(self, k, prices):
        tmp = len(prices)/2
        if k >= len(prices)//2:
            return sum(i-j for i, j in zip(prices[1:], prices[:-1]) if i-j > 0)
        hold, release = [float('-inf')]*(k+1), [0]*(k+1)
        for p in prices:
            for i in range(1, k+1):
                release[i] = max(release[i], hold[i]+p)
                hold[i] = max(hold[i], release[i-1]-p)
        return release[k]

k = 2
prices = [3,2,6,5,0]
sol = Solution()
ret = sol.maxProfit(k,prices)
print(ret)