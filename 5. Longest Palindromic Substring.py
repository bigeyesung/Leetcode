class Solution:
    #brute for sol
    def longestPalindrome(self, s):
        def isPalindrome(s,l,r):
            while (l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        longest = ""
        for ind in range(len(s)):
            for ind1 in range(ind,len(s)):
                if ind1-ind+1>len(longest) and isPalindrome(s,ind,ind1):
                    longest = s[ind:ind1+1]
        return longest

    #improvement sol
    def longestPalindrome1(self, s):
        n=len(s)
        def getLen(l,r):
            while(l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        start=0
        length=0
        for ind in range(n):
            cur = max(getLen(ind,ind),getLen(ind,ind+1))
            if cur<=length:
                continue
            length=cur
            start = ind-(cur-1)//2
        return s[start:start+length]

if __name__ == "__main__":
    sol=Solution()
    s = "bcb"
    ret=sol.getLen2(s,1,1)
    ret1=sol.getLen2(s,1,2)
    ret = sol.longestPalindrome1(s)
    print(ret)