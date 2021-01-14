# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, node, arr):
        if not node:
            return
        self.inorder(node.left,arr)
        arr.append(node.val)
        self.inorder(node.right,arr)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        #In-order search
        arr = []
        self.inorder(root,arr)
        root = TreeNode(arr[0])
        ret=root
        for ind in range(1,len(arr)):
            curNode = TreeNode(arr[ind])
            root.right=curNode
            root=root.right
        return ret

    def increasingBST1(self, root):
        def helper(root, tail = None):
            if not root: 
                return tail
            res = helper(root.left, root)
            root.left = None
            root.right = helper(root.right, tail)
            return res
        
        return helper(root, None)

if __name__ == "__main__":
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node5.left=node3
    node5.right=node6
    sol=Solution()
    ret = sol.increasingBST1(node5)
    while(ret):
        print(ret.val)
        ret=ret.right

def test(node,val):
    if not node:
        return
    #check cur node:
    if node.val==val:
        return node
    else:
        if val<node.val:
            test(node.left,val)
        else:
            test(node.right,val)