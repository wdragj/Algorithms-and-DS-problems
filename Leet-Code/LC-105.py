# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Given two integer arrays preorder and inorder
        # Inorder is the inorder traversal of the binary tree (left, node, right)
        # Preorder is the preorder traverasl of the binary tree (node, left, right)
        # Construct and return the binary tree
        
        # Let first value in preorder be x
        # Values to the left of x in inorder is left
        # Values to the right of x in inorder is right
        
        if not preorder or not inorder: return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # Find the pivot index to partition
        
        # Partition the left subtree of root
        root.left = self.buildTree(preorder[1:1 + mid], inorder[:mid])
        
        # Partition the right subtree of root
        root.right = self.buildTree(preorder[1 + mid:], inorder[1 + mid:])
        
        return root