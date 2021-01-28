"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #T:O(n)
        #S:O(h):tree height
        # def dfs(root, arr):
        #     if not root:
        #         return
        #     if root.children:
        #         for child in root.children:
        #             dfs(child,arr)
        #     arr.append(root.val)
        # arr = []
        # if root:
        #     dfs(root, arr)
        # return arr
        
        #T:O(N)
        #S:O(N)
        def bfs(root):
            if not root:
                return []
            arr = []
            stack = [root]
            while(stack):
                node = stack.pop()
                if node.children:
                    for child in node.children:
                        stack.append(child)
                arr.append(node.val)
            arr.reverse()
            return arr
        return bfs(root)
                