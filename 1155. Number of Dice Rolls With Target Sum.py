class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int):
        dp = [[0] * (target+1) for _ in range(d+1)]
        dp[0][0] = 1 # dp[#dice][target] = total count
        for i in range(1, d+1):
            for tar in range(1, target+1):
                SUM = 0
                for num in range(1, f+1):
                    left = tar-num
                    if left >= 0:
                        SUM+=dp[i-1][left]
                dp[i][tar]=SUM
                print("#dice: %d, target: %d, sum: %d" %(i,tar,SUM))
        return dp[-1][-1] % (10**9 + 7)

    def mytest(self, dice, f, target):
        dp = []
        for dice in range(dice+1):
            tmp = []
            for tar in range(target+1):
                tmp.append(0)
            dp.append(tmp)
        #for 1 dice solution
        dp[0][0]=1
        for i in range(1,dice+1):
            for tar in range(1,target+1):
                SUM=0
                for num in range(1,f+1):
                    if tar-num>=0:
                        SUM+=dp[i-1][tar-num]
                dp[i][tar]=SUM
        return dp[-1][-1]%(10**9+7)
if __name__ == "__main__":
    sol = Solution()
    d = 2 
    f = 6
    target = 7
    ret = sol.mytest(d,f,target)
    print(ret)