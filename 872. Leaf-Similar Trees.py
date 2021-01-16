# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def GetLeaf(self, node):
        #use pre-order but only for leaf
        def preOrder(node):
            if not node:
                return
            else:
                if (not node.left) and (not node.right):
                    arr.append(node.val)
                    return
                preOrder(node.left)
                preOrder(node.right)

        # arr = []
        # preOrder(node)
        # return arr
    
        def preOrderBfs(node):
            if not node:
                return 
            stack = [node]
            ret = []
            while(stack):
                node=stack.pop()
                #leaf node
                if not node.left and not node.right:
                    ret.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return ret
        return preOrderBfs(node)
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr1 = self.GetLeaf(root1)
        arr2 = self.GetLeaf(root2)
        print("arr1: ",arr1)
        print("arr2: ",arr2)
        if arr1 == arr2:
            return True
        else:
            return False

if __name__ == "__main__":
    node3=TreeNode(3)
    node5=TreeNode(5)
    node1=TreeNode(1)
    node6=TreeNode(6)
    node2=TreeNode(2)
    node3.left=node5
    node3.right=node1
    node5.left=node6
    node5.right=node2
    sol=Solution()
    arr=sol.GetLeaf(node3)
    print(arr)