class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                ss = s[i:j]
                if ss == ss[::-1]:
                    count += 1
        return count

    def countSubstrings1(self, s):
        n = len(s)
        dp = [[0] * n for i in range(n)]
        count = 0
        for end in range(n):
            dp[end][end] = 1
            count += 1
            for start in range(end):
                if s[start] == s[end] and (start+1 >= end-1 or dp[start+1][end-1]):
                    count += 1
                    dp[start][end] = 1
        return count

    def countSubstrings2(self, s: str) -> int:
        count = 0
        n = len(s)
        if not n:
            return 0
        for i in range(n):
            count += 1
            left, right = i-1, i+1
            while right < n and s[right] == s[i]:
                right+=1
                count+=1
            while left >=0 and right < n and s[left] == s[right]:
                count+=1
                left-=1
                right+=1
        return count

if __name__ == "__main__":
    sol = Solution()
    ret = sol.countSubstrings1("aaa")