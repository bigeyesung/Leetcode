def removeOuterParentheses(S):
    cnt = 0
    ans = ""
    begin = 0
    
    for i, s in enumerate(S):
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0: 
            ans += S[begin+1:i]
            begin = i+1
    return ans


test = "(()())(())"
ans = removeOuterParentheses(test)
