# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):

        def deep(root):
            if not root:
                return 0, None
            l, r = deep(root.left), deep(root.right)
            if l[0] > r[0]: 
                return l[0] + 1, l[1]
            elif l[0] < r[0]: 
                return r[0] + 1, r[1]
            else: 
                return l[0] + 1, root
        return deep(root)[1]


node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3.left = node5
node3.right = node1
node5.right = node2

sol = Solution()
res = sol.subtreeWithAllDeepest(node3)
print(res)