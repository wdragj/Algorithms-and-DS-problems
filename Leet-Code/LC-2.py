# Medium

# Brute Force Method

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = [], []
        
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
            
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        
        list1, list2 = list(reversed(list1)), list(reversed(list2))
        sum1 = "".join(list1)
        sum2 = "".join(list2)
        totsum = reversed(str(int(sum1) + int(sum2)))
        list3 = []
        for n in totsum:
            list3.append(int(n))

        dummy = ListNode()
        sumNode = dummy
        
        print(list1)
        print(list2)
        
        for i in range(len(list3)):
            sumNode.next = ListNode(list3[i])
            sumNode = sumNode.next
        
        return dummy.next

# Using Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculation
            val = v1 + v2 + carry # Sum of v1, v2, and carry if there is one from prev iter
            carry = val // 10 # Carry is calculated to be used for next iter
            val %= 10 # Actual value
            
            # Creating a new node with the sum value
            cur.next = ListNode(val)
            
            # Update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next