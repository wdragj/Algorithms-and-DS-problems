# Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of linked list
        cur = slow.next # Start of second half
        prev = slow.next = None # The next value of the end of first half should be Null
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # merge the first half and second half
        start = head
        end = prev
        
        while end:
            temp1, temp2 = start.next, end.next
            
            start.next = end
            end.next = temp1
            
            start, end = temp1, temp2