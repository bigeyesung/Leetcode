import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        #find target node
        #find distance below node
        #find distance above node
        conn = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        connect(None, root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(K):
            # bfs = [y for x in bfs for y in conn[x] if y not in seen]
            new_level = []
            for x in bfs:
                for y in conn[x]:
                    if y not in seen:
                        new_level.append(y)
            bfs = new_level
            # add all the values in bfs into seen
            seen = seen | set(bfs)
        return bfs

node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node2 = TreeNode(2)
node7 = TreeNode(7)
node4 = TreeNode(4)
node3.left = node5
node3.right = node1
node5.right = node2
node2.left = node7
node2.right = node4
sol = Solution()
res = sol.distanceK(node3, node5, 2)
print(res)