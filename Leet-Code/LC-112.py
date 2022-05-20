# Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Given the root of a binary tree and an integer targetSum
        # Return True: If the tree has a root-to-leaf path
        #              Such that adding up all the values along the path equals targetSum
        # Else return False
        
        # Use DFS to recursively check if a root-to-leaf path exists such that the sum equals targetSum
        
        def dfs(node, curSum):
            if node:
                curSum += node.val
                print(curSum)
                
                # If curSum ever equals targetSum and it is the leaf node
                if curSum == targetSum and not node.left and not node.right:
                    return True
                
                # If there is even ONE path
                # In which the sum of nodes from root to leaf = targetSum, return True
                return dfs(node.left, curSum) or dfs(node.right, curSum)
            else:
                return False
        
        return dfs(root, 0)