# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #T:O(N)
    #S:O(H):tree height
    def levelOrderBottomDFs(self, root):
        def dfs(root, level):
            if not root:
                return
            # if first time: create a empty list 
            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)

            level+=1
            dfs(root.left, level)
            dfs(root.right, level)
        ans = []
        dfs(root,0)
        return ans
            
    #T:O(N+Nlog(N))
    #S:O(N)
    def levelOrderBottom(self, root):
        #create a queue
        que = []
        #create a arr
        ans = []
        #check root is not empty
        if not root:
            return ans
        #while queue not empty:
        else:
            que.append(root)
        while(que):
            countNode = len(que)
        #   while queue nums not empty(same level nodes):
            sameLevel = []
            while(countNode!=0):
        #       put the node to the list
                curNode = que.pop(0)
                sameLevel.append(curNode.val)
        #       put the child to the queue
                if curNode.left:
                    que.append(curNode.left)
                if curNode.right:
                    que.append(curNode.right)
                countNode-=1
            ans.append(sameLevel)
        
        #bottom-up level order
        ans.reverse()
        #return arr
        return ans