# Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Given the root of a binary tree
        # Return the preorder traversal of its nodes' values
        # Pre-Order Traverasl: node > left > right
        # 1. Check node
        # 2. Check left
        # 3. Check right
        # Solve with DFS
        
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, node, res):
        if node:
            res.append(node.val) # 1. Check node
            self.dfs(node.left, res) # 2. Check left
            self.dfs(node.right, res) # 3. Check right