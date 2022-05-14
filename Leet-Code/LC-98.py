# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 1. Left subtree is less than node AND Right subtree is greater than node (BST)
        # 2. Left and right subtree must also be BST (Lbst, Rbst)

        def valid(node, left, right):  # node, left boundary, right boundary
            if not node:  # If node is null, True
                return True

            # if node is NOT less than right boundary and greater than left boundary, False
            if not(node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # We don't know the value of root so set its left boundary to -infinity and right to infinity
        return valid(root, float("-inf"), float("inf"))
