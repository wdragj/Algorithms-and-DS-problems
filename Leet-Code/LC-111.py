# Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Given a binary tree
        # Find its minimum depth
        # The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node
        
        # Recursively find the minimum depth of left and right subtree
        # 1. Base: Depth of null node is 0
        # 2. If both left and right, return the min
        # 3. If one sided, return the max
        
        # Case 1
        if not root: return 0
        
        if root.left and root.right: # Case 2
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else: # Case 3
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))