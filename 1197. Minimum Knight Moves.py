from collections import deque


class Solution(object):
    def minKnightMoves(self, target_x, target_y):

        # as is is symmetric, we only consider x,y >=0 
        target_x = abs(target_x)
        target_y = abs(target_y)

        q = deque()
        seen = set()

        q.append((0, 0, 0))

        while q:
            xx, yy, step = q.popleft()
            if xx == target_x and yy == target_y:
                return step
            if (xx, yy) in seen:
                continue
            seen.add((xx, yy))
            # lower_bound:a threshold for not allow map to go x,y <=0 cases
            lower_bound = 0
            for dx, dy in [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]:
                if lower_bound < dx + xx <= target_x and lower_bound < dy + yy <= target_y:
                    q.append((dx + xx, dy + yy, step + 1))

sol = Solution()
ret = sol.minKnightMoves(2,1)
print(ret)

