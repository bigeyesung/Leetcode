class Solution:
  def subsets(self, nums):
    ans = []

    def dfs(length, ind, curSub):
      #if target length == len of current Subarr-> append
      if length == len(curSub):
        print("cur new subset:", curSub.copy())
        ans.append(curSub.copy())
        return
      #else add more eles to the curSub
      for i in range(ind, len(nums)):
        curSub.append(nums[i])
        print("append: ",nums[i])
        dfs(length, i + 1, curSub)
        curSub.pop()


    #start from length=0 subset: []
    #then length=1 subset:[1],[2],[3]
    #then length=2 subset:[1,2],[1,3],[2,3]
    #then length=3 subset:[1,2,3]
    for length in range(len(nums) + 1):
      dfs(length, 0, [])
    return ans

nums=[1,2,3]
sol=Solution()
ans=sol.subsets(nums)

