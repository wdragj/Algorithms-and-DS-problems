# Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Given an integer array nums, sorted in ascending order
        # Convert it to a height-balanced BST
        # A height-balanced binary tree is a binary tree
        # In which the depth of the two subtrees of every node never differs by more than one
        
        def createTree(l, r):
            if l > r: # If null
                return None
            
            m = (l + r) // 2
            
            root = TreeNode(nums[m])
            root.left = createTree(l, m - 1) # Create left
            root.right = createTree(m + 1, r) # Create right
            
            return root
        
        return createTree(0, len(nums)-1)