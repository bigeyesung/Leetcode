import math
class Solution:
    def calculate(self, s):
        num = 0
        #preSign="+": It is used for the first num to be added to stack
        preSign = '+'
        #s+='+': Is is used for the last num to be added to stack
        s+='+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                    continue
            else:
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif preSign == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num))
                num = 0
                preSign = c
        return sum(stack)

if __name__=="__main__":
    sol=Solution()
    s="3+2+2"
    ret=sol.calculate(s)
    print(ret)
