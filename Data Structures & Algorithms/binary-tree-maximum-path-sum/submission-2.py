# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=float('-inf')# because -ve numbers bhi hian
        def dfs(node):
            nonlocal ans 
            if not node :
                return 0
            # traversel dfs 
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            ans=max(ans,left+right+node.val)
            return node.val+max(left,right)
        dfs(root)
        return int(ans)


