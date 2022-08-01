# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Given the root of a binary tree
        # Return the postorder traversal of its nodes' values
        # Post-Order Traversal: left > right > node
        # Use DFS to recursively find postorder traversal
        # 1. Check left
        # 2. Check right
        # 3. Check node
        
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res) # 1. Check left
            self.dfs(node.right, res) # 2. Check right
            res.append(node.val) # 3. Check node