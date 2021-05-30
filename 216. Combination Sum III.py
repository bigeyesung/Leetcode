class Solution:
    def combinationSum3(self, length, totalSum):
        totalSubs = []
        
        def backtrack(startInd, curSub, totalSum):
            #length of curSub== target length and totalSum is 0
            if len(curSub) == length and totalSum == 0:
                totalSubs.append(curSub.copy())
                return
            #if during iteration, totalSum<0 or have enough eles in subArr but not fufill requiremnt, return
            elif totalSum < 0 or len(curSub) == length:
                return
            #choose number 1~ 9, no repeat number
            #add more eles to the curSub, do Dfs(getSubArr) 
            for i in range(startInd, 9):
                curSub.append(i+1)
                backtrack(i+1, curSub, totalSum-(i+1))
                curSub.pop()
        
        backtrack(0, [], totalSum)
        return totalSubs
if __name__ == "__main__":
    sol=Solution()
    length = 2 #total length
    totalSum = 6 #totalSum
    ret=sol.combinationSum3(length,totalSum)
    print(ret)

                    