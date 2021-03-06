class Solution:
    def spiralMatrixIII(self, R, C, x, y):

        res = []
        dx, dy, n = 0, 1, 0
        while len(res) < R * C:
            # walk a specific distance D then turn around
            # D:[1,1,2,2,3,3,4,4............etc]
            for i in range(int(n / 2 + 1)):
                if 0 <= x < R and 0 <= y < C:
                    res.append([x, y])
                x, y = x + dx, y + dy
            dx, dy, n = dy, -dx, n + 1
        return res

sol = Solution()
res = sol.spiralMatrixIII(1,4,0,0)
print(res)