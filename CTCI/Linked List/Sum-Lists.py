# You have two numbers represented by a linked list, where each node contains a single digit
# The digits are stored in reverse order, such that the 1's digit is at the head of the list
# Write a function that adds the two numbers and returns the sum as a linked list
# Ex) Input:   (7 > 1 > 9) + (5 > 9 > 2), which is 617 + 295 = 912
#     Output:  (2 > 1 > 9), which is 912
# FOLLOW UP
# Suppose the digits are stored in forward order
# Repeat the above problem
# Ex) Input:   (6 > 1 > 7) + (2 > 9 > 5), which is 617 + 295 = 912
#     Output:  (9 > 1 > 2), which is 912

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# From LeetCode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:    
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry # Total sum of v1 + v2 + carry
            carry = val // 10 # Carry value which is val // 10
            val %= 10 # Actual value (1-digit) which is val mod 10
            
            # Create new node
            cur.next = ListNode(val)
            
            # Update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next