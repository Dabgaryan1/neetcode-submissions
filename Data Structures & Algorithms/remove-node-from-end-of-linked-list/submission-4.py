# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   #dummy node before head
        left, right = dummy, head   #left node at dummy, right node at head 

        #move right n times through linked list
        for i in range(n):
            right = right.next

        #simultaneously move left & right until right is null
        while right:
            left = left.next
            right = right.next
        
        #delete left.next(node at position n from the end of the list)
        left.next = left.next.next

        #dummy.next is at the head so return it
        return dummy.next