# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #iterate the list in order to get the middle node(1st,2nd) parts
        #while the iteration, we can reverse 1st part list
        #after that, we compare 1st and 2nd part to see if they are the same
        
        #1->3->1
        #1->3->3->1
        
        if not head:
            return False
        slow,fast,cur=head,head,head
        prev=None
        num=0
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
            num+=1
        
        #after that, slow points to the middle
        #check even case and odd cases
        
        #if odd cases: -> check start from slow ptr
        if num%2==1:
            if slow.next:
                slow=slow.next
            while(prev and slow):
                if prev.val!=slow.val:
                    return False
                else:
                    prev=prev.next
                    slow=slow.next
            return True
        else:
            if slow.next:
                slow=slow.next
            while(prev and slow):
                if prev.val!=slow.val:
                    return False
                else:
                    prev=prev.next
                    slow=slow.next
            return True

if __name__ == "__main__":
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(2)
    node4=ListNode(2)
    node5=ListNode(1)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5


    sol=Solution()
    ret=sol.isPalindrome(node1)