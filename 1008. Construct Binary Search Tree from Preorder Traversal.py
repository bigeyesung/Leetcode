import bisect
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder: 
            return
        root = TreeNode(preorder[0])
        stack = [root]
        i = 1
        while i < len(preorder) and stack:
            node = stack.pop()
            v = preorder[i]          
            if v < node.val:
                node.left = TreeNode(v)
                i += 1
                stack.append(node)
                stack.append(node.left)
            else:
                while stack and stack[-1].val < v:
                    node = stack.pop()
                node.right = TreeNode(v)
                i += 1
                stack.append(node.right)                
                
        return root




if __name__ == "__main__":
    sol=Solution()
    preorder=[8,5,1,7,10,12]
    sol.bstFromPreorder(preorder)