# Definition for a binary tree node.
'''
Use BFS to do a level order traversal,
add childrens to the bfs queue,
until we met the first empty node.

For a complete binary tree,
there should not be any node after an empty one.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root):
        bfs = [root]
        ind = 0
        while(bfs[ind]):
            bfs.append(bfs[ind].left)
            bfs.append(bfs[ind].right)
            ind += 1
        tmp = any(bfs[ind:])
        return not any(bfs[ind:])
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

sol = Solution()
ret = sol.isCompleteTree(node1)
print(ret)