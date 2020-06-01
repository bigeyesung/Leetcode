from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        seen = set()
        q= deque()
        n = len(grid)-1

        if grid[0][0] or grid[n][n]:
            return -1
        q.append((0,0,0))
        while q:
            xx,yy,step = q.popleft()
            if xx == n and yy ==n:
                return step
            if (xx,yy) in seen:
                continue
            seen.add((xx,yy))

            for dx,dy in [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]:
                if 0<=xx+dx<=n and 0<=yy+dy<=n and grid[xx+dx][yy+dy]==0:
                    q.append((xx+dx,yy+dy,step+1))
        return -1

grid = [[0,1],[1,0]]
sol = Solution()
ret = sol.shortestPathBinaryMatrix(grid)
print(sol+1)

        
