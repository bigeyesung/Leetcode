# iterate char in a string
# save in stack and temp var cur
# if c is "(": push in stack
# if c is ")":pop stack
# else: add cur
class Solution:
    def minRemoveToMakeValid(self, s):
        stack, cur = [], ""
        for ch in s:
            if ch == "(":
                stack.append(cur)
                cur = ""
            elif ch == ")":
                if stack:
                    cur = stack.pop() + "("+ cur + ")"
            else :
                cur += ch
        while stack:
            cur = stack.pop() + cur 
        return cur
if __name__ == "__main__":
    sol = Solution()
    ret = sol.minRemoveToMakeValid("))((")
    print(ret)


