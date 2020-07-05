class Solution:
    def minAddToMakeValid(self, S):
        # find a way to remove parentheses string
        # cound the remaining nums
        stack = []
        for c in S:
            if c == "(":
                stack.append(c)
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)

sol = Solution()
ret = sol.minAddToMakeValid("(()()()())))")
print(ret)
