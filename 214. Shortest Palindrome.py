def shortestPalindrome(s):
    A=s+"*"+s[::-1]
    cont=[0]
    for i in range(1,len(A)):
        index=cont[i-1]
        while(index>0 and A[index]!=A[i]):
            index=cont[index-1]
        cont.append(index+(1 if A[index]==A[i] else 0))
    tmp = s[cont[-1]:]
    tmp2 = tmp[::-1]
    return tmp2 + s

def shortestPalindrome1(s):
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s

ret = shortestPalindrome1("abc")
print(ret)