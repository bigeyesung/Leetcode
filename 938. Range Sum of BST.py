class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans=0

    #Time: O(N)
    #Space: O(H): where H is the maximum height of the tree
    def startBST(self, node: TreeNode, low: int, high: int):
        #if not node->return
        if not node:
            return 0
        #else: check cur val in range or not
        cur,ret1,ret2=0,0,0
        if low<=node.val<=high:
            cur =node.val
        #This BST, so we can check the range to decide to go further or not
        if node.val>=low:
            ret1=self.startBST(node.left,low,high)
        #This BST, so we can check the range to decide to go further or not
        if node.val<=high:
            ret2=self.startBST(node.right,low,high)

        return ret1+ret2+cur

        #Time: O(N)
        #Space: O(w) where w is the maximum width of the tree
    def startBfs(node,low,high):
        stack = [node]
        res = 0
        while(stack):
            curNode=stack.pop()
            if low<=curNode.val<=high:
                res+=curNode.val
            if curNode.val<=high and curNode.right:
                stack.append(curNode.right)
            if curNode.val>=low and curNode.left:
                stack.append(curNode.left)
        return res    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        # func to traverse the tree
        ret = self.startBST(root, low, high)
        return ret

node10 = TreeNode(10)
node5 = TreeNode(5)
node15 = TreeNode(15)
node3 = TreeNode(3)
node10.left = node5
node10.right = node15
node5.left = node3

sol = Solution()
sol.rangeSumBST(node10, 5,8)