import math
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #iterate 2 linked list
        #judge if needing carry
        carry=0
        l3 = ListNode(None)
        index = l3
        while(l1 or l2 or carry !=0):
            val=0
            if l1:
                val = val + l1.val
                l1=l1.next
            if l2:
                val = val + l2.val
                l2=l2.next  
            val = val + carry
            carry = 0              
            index.val=int(val% math.pow (10, 1))
            carry = int(val/ math.pow (10, 1))
            if (l1 or l2 or carry != 0):
                index.next = ListNode(None)
                index=index.next 
        return l3   