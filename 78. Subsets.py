class Solution:
  def subsets(self, nums):
    ans = []
    def dfs(n, s, cur):
      if n == len(cur):
        ans.append(cur.copy())
        return
      for i in range(s, len(nums)):
        cur.append(nums[i])
        print("n: ",n)
        print("i+1: ",i+1)
        dfs(n, i + 1, cur)
        cur.pop()
    for i in range(len(nums) + 1):
      if i==3:
        print("pai")
      dfs(i, 0, [])
    return ans

nums=[1,2,3]
sol=Solution()
ans=sol.subsets(nums)