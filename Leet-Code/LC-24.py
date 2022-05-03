# Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            # save ptrs
            nxtpr = curr.next.next # the next pair
            second = curr.next # original second
            
            # reverse this pair
            second.next = curr # second's next is head
            curr.next = nxtpr # head's next is next pair
            prev.next = second # new head 
            
            # update ptrs
            prev = curr
            curr = nxtpr
        
        return dummy.next