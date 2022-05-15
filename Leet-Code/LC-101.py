# Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Given root of a binary tree
        # Check if it is a mirror of itself
        # Symmetric around its center
        
        # If node is null return True
        if not root: return True 
        
        return self.check(root.left, root.right)
        
    def check(self, left, right):
        # Both left and right are null
        if not left and not right:
            return True
        
        # If only one of them is null
        if not left or not right:
            return False
        
        # Values are diff
        if left.val != right.val:
            return False
        
        # Check left's left and right's right
        l = self.check(left.left, right.right)
        
        # Check left's right and right's left
        r = self.check(left.right, right.left)
        
        return l and r