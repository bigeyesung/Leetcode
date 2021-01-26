# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1, t2):
        #T: O(n): n is max node of (t1,t2)
        #S: O(h): height of tree
        #traverse two trees at same time(recursive)
        #t1 is empty
        if not t1:
            return t2
        #t2 is empty
        if not t2:
            return t1
        #none of above cases
        t = TreeNode(t1.val+t2.val)
        t.left = self.mergeTrees(t1.left,t2.left)
        t.right =self.mergeTrees(t1.right,t2.right)
        return t
    def mergeTreesBFS(self,t1,t2):
        #T:O(n)
        #S:O(n)
        #BFS to solve it
        if not t1:
            return t2
        #create a stack for t1,t2
        stack = [(t1,t2)]
        #while stack exists:
        while(stack):
            #check both trees exist
            t1Tmp,t2Tmp = stack.pop()
            if not t1Tmp or not t2Tmp:
                continue
            #if they are, then sum up results to t1
            t1Tmp.val+=t2Tmp.val
            #check t1-left exist:
            if t1Tmp.left:
                #add t1-left,t2-left to stack
                stack.append([t1Tmp.left,t2Tmp.left])
            #t1-left not exist:
            else:
                #t1-left= t2.left
                t1Tmp.left=t2Tmp.left
            #check t1-right exist:
            if t1Tmp.right:
                #add t1-right,t2-right to stack
                stack.append([t1Tmp.right,t2Tmp.right])
            #t1-right not exist:
            else:
                #add t1.right = t2.right
                t1Tmp.right=t2Tmp.right
        return t1
import heapq
if __name__ == "__main__":
#    nums = [5,4,2]
#    nums1 = [5,4,2]
#    heapq.heapify(nums)
#    heapq._heapify_max(nums1)
#    heapq._heappop_max(nums1)
    t1 = []
    t2 = [4,5]
    stack = [[t1,t2]]
    while(stack):
        t1,t2 = stack.pop()
        if not t1 or not t2:
            continue
    print("finish")