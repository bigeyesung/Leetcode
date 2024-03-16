class Solution:
    def combinationSum(self, candidates, target):
        #sol 1
        # def dfs(startIdx, target, subArr, ret):
        #     if target < 0:
        #         return 
        #     if target == 0:
        #         ret.append(subArr.copy())
        #         return 
        #     for ind in range(startIdx,len(candidates)):
        #         subArr.append(candidates[ind])
        #         dfs(ind, target-candidates[ind], subArr, ret)
        #         subArr.pop()
        # ret = []
        # dfs(0, target, [], ret)
        # return ret

        #sol 2
        # Time Complexity: O(M*M*N), N = len(candidates), M = target
        # Space Complexity: O(M*M)
        target_table = [[] for data in range(target+1)] #create table that list all targets(from 0 to target)
        for candidate in candidates:                                  # O(N): for each candidate
            print(f'candidate: {candidate}')
            for num in range(candidate, target+1):#for each candidate, we iterate the loop between c to target(checking remain)                      # O(M): for each possible value <= target
                if num == candidate: 
                    target_table[num].append([candidate])
                for comb in target_table[num-candidate]: #if we want to update target[num], we need to see if target[num-c] is avialble or not
                    target_table[num].append(comb+[candidate]) # O(M) worst: for each combination
        print(target_table)
        return target_table[-1]
    
        target_table = [[] for data in range(target+1)] #create a table list all from 0 to target
        for c in candidates: #iterate all candidate
            for num in range(c,target+1): #for each candidate, we iterate the loop between c to target(checking remain)
                if num == c:
                    target_table[num].append([c])
                for combination in target_table[num-c]:
                    target_table[num].append(combination+[c])
        return target_table[-1]
if __name__=="__main__":
    candidates=[2,3,6,7]
    target=7
    # candidates=[1,2]
    # target=2
    sol=Solution()
    res=sol.combinationSum(candidates,target)
    print(res)