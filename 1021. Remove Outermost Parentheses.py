'''
opened count the number of opened parenthesis.
Add every char to the result,
unless the first left parenthesis,
and the last right parenthesis.
'''

class Solution:    
    def removeOuterParentheses(self, S):
        res, opened = [], 0
        for c in S:
            # >0 means: check 
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)

sol = Solution()
sol.removeOuterParentheses("((()")