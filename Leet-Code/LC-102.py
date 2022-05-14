# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level Order Traversal
        # Return a list of a tree level by level
        
        if not root: # If tree is empty
            return []
        
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q: # Until queue is empty
            qLen = len(q) # Snapshot of the length of queue
            level = [] # Level list to append to
            
            for i in range(qLen): # Iterate for the length of queue at snapshot
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level: res.append(level) # If there are values in level
        
        return res