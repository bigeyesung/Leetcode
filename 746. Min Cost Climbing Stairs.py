class Solution:
    def minCostClimbingStairs(self, cost):

        dp = [0]*(len(cost))
        dp[0], dp[1]=cost[0], cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])
        
        return min(dp[-2], dp[-1])
    def test(self, cost):
        for ind in range(2,len(cost)):
            cost[i] = min(cost[ind]+cost[ind-1], cost[ind]+cost[ind-2])
        return min(cost[-1], cost[-2])

if __name__ == "__main__":
    cost = [10, 15, 20]
    sol = Solution()
    ret = sol.test(cost)
    print(ret)