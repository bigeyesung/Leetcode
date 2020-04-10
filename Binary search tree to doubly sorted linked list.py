class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treeToDoublyList(root):
    if (not root):
        return None
    head = TreeNode(None)
    pre = TreeNode(None)
    inorder(root, pre, head)
    pre.right = head
    head.left = pre
    return head
    
def inorder(node, pre, head):
    if (not node):
        return
    print(node.val)
    inorder(node.left, pre, head)
    if (not head):
        head = node
        pre = node
    else:
        pre.right = node
        node.left = pre
        pre = node
    
    inorder(node.right, pre, head)

node1 = TreeNode(1)    
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node4.left = node2
node4.right = node5
node2.left= node1
node2.right = node3

head = treeToDoublyList(node4)
tmp = head.val
while(not head):
    print("val: ",head.val)
    head = head.right