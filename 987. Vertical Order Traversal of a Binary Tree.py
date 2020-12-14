import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode):
        self.ver = collections.defaultdict(list)
        def dfs(node, x, y):
            if node:
                self.ver[x].append([y, node.val])
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)
        dfs(root, 0, 0)
        res = []
        for _, arr in sorted(self.ver.items()):
            tmp = map(lambda x: x[1], sorted(arr))
            res.append(list(tmp))
        return res
        # return [list(map(lambda x: x[1], sorted(arr))) for x, arr in sorted(self.ver.items())]  

node9 = TreeNode(9)
node3 = TreeNode(3)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

sol = Solution()
ret = sol.verticalTraversal(node3)
print(ret)