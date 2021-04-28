# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff2(self, root):
        def dfs(node, cur_max, cur_min):
            if not node:
                return cur_max - cur_min
            else:
                cur_max = max(cur_max, node.val)
                cur_min = min(cur_min, node.val)
                left = dfs(node.left, cur_max, cur_min)
                right = dfs(node.right, cur_max, cur_min)
                return max(left, right)
            
        if not root:
            return 0
        else:
            return dfs(root, root.val, root.val)
    def maxAncestorDiff(self, root):
        #question:
        #root = [8,3,10,1,6,null,14,null,null,4,7,13] -> 7
        
        #data
        #input: treeNode:, integer only, unique num, min size: 2
        #ouput: int: positive num
        
        #seudo code:
        #iterate the tree and create a connect table
        #while iteration, we keep the leaf node
        
        #iterate the leaf node:
        #   for each iteration, we update minVal, maxVal. curAbs= maxVal-minVal
        #   for each iteration, we compare curAbs to find max abs val
        #return maximum abs val
        
        connect={}
        leafs=[]
        maxAbs=0
        def Traversal(root):
            if not root:
                return
            queue=[root]
            
            while(queue):
                levelCnt=len(queue)
                while(levelCnt!=0):
                    #sth
                    curNode=queue.pop(0)
                    print("cur:",curNode.val)
                    if curNode.left:
                        connect[curNode.left.val]=curNode.val
                        queue.append(curNode.left)
                    if curNode.right:
                        connect[curNode.right.val]=curNode.val
                        queue.append(curNode.right)
                    if not curNode.left and not curNode.right:
                        leafs.append(curNode.val)
                    levelCnt-=1
        Traversal(root)
        for num in leafs:
            minVal=float("inf")
            maxVal=0
            curNum=num
            while(connect.get(curNum)!=None):
                parent=connect[curNum]
                minVal=min(minVal,curNum)
                minVal=min(minVal,parent)
                maxVal=max(maxVal,curNum)
                maxVal=max(maxVal,parent)
                curNum=parent
            maxAbs=max(maxAbs,maxVal-minVal)
        return maxAbs
                
if __name__=="__main__":
    sol=Solution()
    node1=TreeNode(1)
    node2=TreeNode(2)
    node0=TreeNode(0)
    node3=TreeNode(3)
    node1.right=node2
    node2.right=node0
    node0.left=node3
    sol=Solution()
    ret=sol.maxAncestorDiff(node1)