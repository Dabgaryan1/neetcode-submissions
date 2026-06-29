# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        L1, L2 = l1, l2

        carry = 0
        while L1 and L2:
            summ = carry + L1.val + L2.val
            if summ >= 10:
               cur.next = ListNode(summ - 10)
               carry = 1
            else:
                cur.next = ListNode(summ)
                carry = 0
            L1 = L1.next
            L2 = L2.next
            cur = cur.next
        
        #L1 not empty
        while L1:
            summ = L1.val + carry
            if summ == 10:
                cur.next = ListNode(0)
            else:
                cur.next = ListNode(summ)
                carry = 0
            L1 = L1.next
            cur = cur.next

        #L2 not empty
        while L2:
            summ = L2.val + carry
            if summ == 10:
                cur.next = ListNode(0)
            else:
                cur.next = ListNode(summ)
                carry = 0
            L2 = L2.next
            cur = cur.next
        #carry leftover
        if carry == 1:
            cur.next = ListNode(1)
        return head.next