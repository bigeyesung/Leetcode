class Solution:
    '''
    Explanation
        Save all time points and the change on current capacity
        Sort all the changes on the key of time points.
        Track the current capacity and return false if negative
    Complexity
        Time O(NlogN)
        Space O(N)
    '''
    def carPooling(self, trips, capacity):
        tmp = []
        for x in trips:
            tmp.append([x[1],x[0]])
            tmp.append([x[2],-x[1]])
        tmp = sorted(tmp)
        # [start, num]: to decrease capacity
        # [end, - start]: to increase capacity
        for i, v in sorted(x for num, start, end in trips for x in [[start, num], [end, - start]]):
            capacity -= v
            if capacity < 0:
                return False
        return True

trips = [[2,1,5],[3,3,7]]
capacity = 4
sol = Solution()
ret = sol.carPooling(trips, capacity)