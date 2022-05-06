# Implement an algorithm to delete a node in the middle
# Ex) Any node but the first and last node, not necessarily the exact middle of a singly linked list, given only access to that node
# Ex) Input: the node c from the linked list ( a -> b -> c -> d -> e -> f )
#     Result: nothing is returned, but the new linked list looks like ( a -> b -> d -> e -> f )

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def delete_middle(self, head: Node):
    slow = fast = head
    prev = None

    # Runner method // Slow and Fast pointers
    while fast and fast.next and fast.next.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    
    # Deletion of the middle node
    prev.next = prev.next.next

    # Check solution
    while head:
      print(head.val, end=" ")
      head = head.next

# Tests
nodelast = Node(6)
node5 = Node(5, nodelast)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

test = node1

while test:
  print(test.val, end=" ")
  test = test.next

print()
Solution().delete_middle(node1)