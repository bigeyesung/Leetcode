# create depth table (depth: list of the depth)
# for-loop the list:
# if ele is int->put in in depth table
# if not: go to further level


def myfunc(arr):
    table = {}
    level = 0
    ret = helper(arr, table, level+1)

def helper(arr, table, level):
    table[level] = []
    for ele in arr:
        if ele is int:
            table[level].append(ele)
        else:
            helper(ele, table, level+1)


class Solution():
    def depthSumInverse(self, nestedList):

        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def level(nestedList,height):
            self.level = max(height, self.level)
            for item in nestedList:
                if not item.isInteger():
                    level(item.getList(), height + 1)

        def dfs(nestedList, height):
            for item in nestedList:
                if item.isInteger():
                    self.res += item.getInteger() * height
                else:
                    dfs(item.getList(),height - 1)
    
        self.level = 1
        self.res = 0
        level(nestedList,1)
        dfs(nestedList, level)
        return self.res

arr = [[1,1],2,[1,1]]
sol = Solution()
ret = sol.depthSumInverse(arr)
print(ret)

