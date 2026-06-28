# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, skip)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # option 1: rob this node
            rob = node.val + left[1] + right[1]
            
            # option 2: skip this node
            skip = max(left) + max(right)
            
            return (rob, skip)
        
        return max(dfs(root))