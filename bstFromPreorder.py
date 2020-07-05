import bisect
my_list = ["how","are","u"]
a = " ".join(my_list)
b = "".join(my_list)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bstFromPreorder(preorder):
    #first num is root
    #inset left node until find the next_num > cur_num
    #insert right node
    def helper(i, j):
        if i == j: return None
        root = TreeNode(preorder[i])
        mid = bisect.bisect(preorder, preorder[i], i + 1, j)
        root.left = helper(i + 1, mid)
        root.right = helper(mid, j)
        return root
    return helper(0, len(preorder))

l1 - [1,2,4,5]
bisect.bisect_left()

l = [1, 3, 7, 5, 6, 4, 9, 8, 2]

result = []
for e in l:
    bisect.insort(result, e)

print(result)

root = bstFromPreorder(arr)