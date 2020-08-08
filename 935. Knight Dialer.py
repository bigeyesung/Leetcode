class Solution:
    def knightDialer(self, N):
        # initial stay in 9 different places (start point)
        # for N-1 hops: 
        # hop to different numbers
        c = 10**9+7
        next_step = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        dp = [1]*10
        for i in range(N-1):
            new_dp = [0]*10
            for j in range(10):
                for n in next_step[j]:
                    new_dp[j] += dp[n]
            dp = new_dp
        return sum(dp)%c


    def myfunc(self, N):
        c = 10**9+7
        next_step = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]       
        dp = [1]*10
        for times in range(N-1):
            newdp = [0]*10
            for j in range(10):
                for n in next_step[n]:
                    newdp[j]+=dp[n]
            dp= newdp
sol = Solution()
ret = sol.knightDialer(2)
print(ret)