
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    #recursive
    #T:O(n)
    #S:O(h):tree height
    def preorder(self, root):
        def Dfs(node,arr):
            if not node:
                return
            
    def preorderDfs(self, node,arr):
        if not node:
            return
        #add cur node to arr
        arr.append(node.val)
        #iterate its child
        if node.children:
            for child in node.children:
                self.preorderBfs(child,arr)
    #iterative
    #T:O(n)
    #S:O(n)
    def preorder(self, root):
        arr = []
        if not root:
            return arr
        stack = [root]
        while(stack):
            curNode= stack.pop()
            arr.append(curNode.val)
            if curNode.children:
                for child in curNode.children[::-1]:
                    stack.append(child)
        return arr
if __name__ == "__main__":

    node5=Node(5)
    node6=Node(6)
    node2=Node(2)
    node3=Node(3,[node5,node6])
    node4=Node(4)
    node1=Node(1,[node3,node2,node4])
    sol=Solution()
    arr = []
    sol.preorderBfs(node1,arr)
    print(arr)