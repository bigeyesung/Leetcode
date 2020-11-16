class Solution:
    def divisorGame(self, N: int) -> bool:       
        if N <= 1:
            return False
        
        dp = [False] * (N + 1)
        
        for i in range(2,N+1):
            # suppose N = i
            print("i: ", i)
            for j in range(1, i // 2 + 1):
                print("j: ", j)
                if i % j == 0: # choosing x = j
                    newN = i - j
                    print("newN: ", newN)
                    if dp[newN] == False:
                        dp[i] = True
        
        return dp[N]
#Build a dynamic programming array bottom up from 1 to N.
#For each index i, find all factors of j that divide i evenly, 
#and see if we can guarantee a win. (That is, see if there exists dp[i-j] that is False) If so, set it to true.
#Finally, return dp[N].

if __name__ == "__main__":
    sol = Solution()
    ret = sol.divisorGame(4)
    print(ret)