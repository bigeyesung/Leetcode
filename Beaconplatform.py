#did not pass the exam due to Q2 and Q3 are not correct

#1:Given a and b strings, find a string index on b and return the first left one
#e.g. a = 52
#e.g. b = 78529632
#index = 2(starting from 0)
def checkindex(a,b):
    a = str(a)
    b = str(b)
    ind = b.find(a)
    return ind
#2:Given a range of numbers a and b, b is included.
#find the number between them can be assembled by 2 adjacent numbers"
#e.g.12=3*4, 20=4*5
def checkrange(a,b):
    ret = []
    for num in range(a,b+1):
        tmp = int(num**0.5)
        if tmp*(tmp+1)==num:
            ret.append(num)
    return ret
def checkrange2(a,b):
    ret = []
    for num in range(a,b+1):
        tmp = (4*num+1)**0.5-1
        if tmp%2==0:
            ret.append(num)
    return ret
#3:Given a tree, finding paths from root to leaf, find the path contains the maximum length, and
#no repeated node number
#   ( 1 )
#   /  \
#  (2) (3)
#  /     \  
# (2)    (4)
#the above answer is 3 (1,3,4) as (1,2,2) is repeated.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self,root):
        #Time:O(N+m)
        #Space:O(H):tree height
        def find(node):
            #node is empty
            if not node:
                return None
            #node is leaf
            elif not node.left and not node.right:
                return [[node.val]]
            #else
            else:
                cur = node.val
                left_lists = find(node.left)
                right_lists = find(node.right)
                combine = []
                if left_lists:
                    for arr in left_lists:
                        arr.append(cur)
                        combine.append(arr)
                if right_lists:
                    for arr in right_lists:
                        arr.append(cur)
                        combine.append(arr)
                return combine
        arrs = find(root)
        length = 0
        for arr in arrs:
            dic = {}
            arr.reverse()
            tmp = 0
            for num in arr:
                if dic.get(num)==None:
                    dic[num]=num
                    tmp+=1
                else:
                    break
            length = max(length,tmp)
        return length
if __name__ == "__main__":
    ret = checkindex(52,785274465)
    print(ret)
    ret = checkrange(0,100000)
    print(len(ret))
    ret = checkrange2(0,100000)
    print(len(ret))
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(2)
    node1.left=node2
    node1.right=node3
    node2.left=node5
    node3.right=node4
    ret = sol.search(node1)
    print(ret)
