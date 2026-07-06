# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i-1])
        return lists[-1]
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode])-> Optional[ListNode]:
        c1, c2 = list1, list2

        dummy = node = ListNode()
        
        while c1 and c2:
            if c1.val <= c2.val:
                node.next = c1
                c1 = c1.next
            else:
                node.next = c2
                c2 = c2.next
            node = node.next
        
        while c1:
            node.next = c1
            c1 = c1.next
            node = node.next
        while c2:
            node.next = c2
            c2 = c2.next
            node = node.next
        return dummy.next
            
                