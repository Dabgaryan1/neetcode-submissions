# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        l1, l2 = list1, list2

        if list1.val <= list2.val:
            head = list1
            l1 = l1.next
        else:
            head = list2
            l2 = l2.next
        curr = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        #finish non empty list
        while l1 is not None:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        while l2 is not None:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        return head
        


            
        
        
        