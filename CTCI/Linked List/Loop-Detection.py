# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
# DEFINITION: Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list
# Ex) Input:   A > B > C > D > E > C [the same C as earlier]
#     Output:  C

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def loop_detection(self, head: Node) -> Node:
    slow = fast = head

    while True:
      slow = slow.next
      fast = fast.next.next

      if slow is fast:
        break
    
    slow = head

    while slow is not fast:
      slow = slow.next
      fast = fast.next
    
    return slow

# Tests
nodeE = Node("E")
nodeD = Node("D")
nodeC = Node("C")
nodeB = Node("B")
nodeA = Node("A")

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeC

print(Solution().loop_detection(nodeA).val)