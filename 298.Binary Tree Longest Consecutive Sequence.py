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
        return find(root)



  
    # method returns length of longest consecutive  
    # sequence rooted at node root
    # #time:O(N)
    # space:O(h)  
    def longestConsecutive(self, root): 



        def longestConsecutiveUtil(root, curLength, expected, res): 
            if (root == None): 
                return
        
            # if root val has one more than its  
            # parent then increase current length  
            if (root.val == expected):  
                curLength += 1
            else: 
                curLength = 1
        
            # update the maximum by current length  
            res[0] = max(res[0], curLength) 
        
            # recursively call left and right subtree  
            # with expected value 1 more than root data  
            longestConsecutiveUtil(root.left, curLength, root.val + 1, res)  
            longestConsecutiveUtil(root.right, curLength, root.val + 1, res) 

        if (root == None):  
            return 0
    
        res = [0]
    
        # call utility method with current length 0  
        test(root, 0, root.val, res)  
    
        return res
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.right = node3
    node3.left = node2
    node3.right = node4
    node4.right = node5
    sol = Solution()
    # ret = sol.search(node1)
    ret1 = sol.longestConsecutive(node1)
    print(ret1[0])