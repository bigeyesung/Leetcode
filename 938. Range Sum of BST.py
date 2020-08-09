class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def calculate(root, L, R):
        # return condition
        if root == None:
            return 0
        else:
            left_sum = self.calculate(root.left, L, R)
            right_sum = calculate(root.right, L, R)
            if root.val <= R and root.val >= L:
                return left_sum + right_sum + root.val
            else:
                return left_sum + right_sum

    def calculate_Preorder(root, L, R, arr):
        if root == None:
            return
        else:
            arr.append(root.val)
            self.calculate_Preorder(root.left, L, R, arr)
            self.calculate_Preorder(root.right, L, R, arr)

    def rangeSumBST(self, root, L, R):

        arr = []
        self.calculate_Preorder(root, L, R, arr)
        print(arr)
        return self.calculate(root,L,R)

node10 = TreeNode(10)
node5 = TreeNode(5)
node15 = TreeNode(15)
node3 = TreeNode(3)
node10.left = node5
node10.right = node15
node5.left = node3

sol = Solution()
sol.rangeSumBST(node10, 5,8)