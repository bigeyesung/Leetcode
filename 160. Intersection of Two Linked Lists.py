# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) -> ListNode:
        p1, p2 = headA, headB
        while p1 != p2:
            # if p1:
            #     print("p1:",p1.val)
            # if p2:
            #     print("p2:",p2.val)
            # print("======")
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
            # if p1:
            #     print("after p1:",p1.val)
            # if p2:
            #     print("after p2:",p2.val)
        # print(p1.val)
        return p1


def test(var):
    var[0]+=5

if __name__ == "__main__":
    apple = [4]
    test(apple)
    print(apple)
    a1 = ListNode(4)
    a2 = ListNode(1)
    a3 = ListNode(8)
    a4 = ListNode(4)
    a5 = ListNode(5)

    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    b4 = ListNode(8)
    b5 = ListNode(4)
    b6 = ListNode(5)
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a4.next=a5

    b1.next=b2
    b2.next=b3
    b3.next=b4
    b4.next=b5
    b5.next=b6

    sol = Solution()
    sol.getIntersectionNode(a1,b1)