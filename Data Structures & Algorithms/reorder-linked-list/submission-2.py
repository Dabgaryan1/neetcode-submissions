# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find halfway point using fast and slow pointer method
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half of list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge two lists
        p, k = head, prev

        while k:
            tmp1, tmp2 = p.next, k.next
            p.next = k
            k.next = tmp1
            p = tmp1
            k = tmp2
        
        

            