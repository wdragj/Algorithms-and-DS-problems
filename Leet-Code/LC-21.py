# Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: # list1.val >= list2.val
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1 is None:
            tail.next = list2
        else:
            tail.next = list1
        
        return dummy.next
                
        # [1 2 3 4]
        # [1 2 3 4 5 6]
        # [1 1 2 2 3 3 4 ]