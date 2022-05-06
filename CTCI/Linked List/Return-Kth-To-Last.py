# Implement an algorithm to find the kth to last element of a singly linked list

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def Kth_To_Last(self, head: Node, k: int) -> Node:
    fast = head

    for _ in range(k):
      if fast:
        fast = fast.next
    
    slow = head

    while fast:
      slow = slow.next
      fast = fast.next
    
    return slow

# Tests
nodelast = Node(6)
node5 = Node(5, nodelast)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

print(Solution().Kth_To_Last(node1, 3).val)
print(Solution().Kth_To_Last(node1, 4).val)
print(Solution().Kth_To_Last(node1, 6).val)
print(Solution().Kth_To_Last(node1, 7).val) # Should result in error as 7th node doesn't exist