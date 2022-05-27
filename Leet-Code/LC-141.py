# Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head # Slow and Fast pointers to the head
        
        while fast and fast.next: # While fast and fast.next is not None
            slow = slow.next # Slow will move 1
            fast = fast.next.next # Fast will move 2
            
            if slow is fast: # If fast catches up to slow // same pointer
                return True # There is a loop
        
        return False # If exited out of while loop // There is no cycle => there is an end