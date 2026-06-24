# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        L1, L2 = list1, list2

        
        while L1 and L2:
            if L1.val <= L2.val:
                node.next = L1
                node = node.next
                L1 = L1.next
            else:
                node.next = L2
                node = node.next
                L2 = L2.next
        while L1:
            node.next = L1
            L1 = L1.next
            node = node.next
        while L2:
            node.next = L2
            L2 = L2.next
            node = node.next
        return dummy.next
            
            

        