class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n=len(jobDifficulty)
        if d>n:
            return -1
        #create dp
        dp=[]
        for ind in range(n+1):
            tmp=[float("inf")]*(d+1)
            dp.append(tmp)
        dp[0][0]=0

        # for each job(1-based)
        for jodId in range(1,n+1):
            #for each day(1-based)
            print("job:",jodId)
            for day in range(1,d+1):
                print("day:",day)
                md=0
                for j in range(jodId-1,day-2,-1):
                    md=max(md,jobDifficulty[j])
                    #dp[i][k]= min diffculty to schedule the first i jobs(1-based) in k days
                    print("dp[jodId][day]",dp[jodId][day])
                    print("dp[j][day-1]",dp[j][day-1])
                    dp[jodId][day]=min(dp[jodId][day],dp[j][day-1]+md)
        return dp[n][d]

if __name__ == "__main__":
    sol=Solution()
    jobDifficulty = [3,4,2]
    d = 2
    ret=sol.minDifficulty(jobDifficulty, d)
    print(ret)