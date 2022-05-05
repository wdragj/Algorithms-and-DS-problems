# Write code to remove duplicates from an unsorted linked list
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def remove_dups(self, head: Node) -> Node:
    cur = head
    prev = None

    nodeset = set()

    while cur:
      if cur.val in nodeset:
        prev.next = cur.next
      else:
        nodeset.add(cur.val)
        prev = cur
      cur = cur.next
    
    return head

# Tests
nodelast = Node(5)
node5 = Node(2, nodelast)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(3, node3)
node1 = Node(4, node2)

remdup = Solution().remove_dups(node1)

while remdup:
  print(remdup.val, end="")
  remdup = remdup.next