# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs traversel 
        # the max val toh root ki honi chaiye 
        def dfs(node,maxVal):
            if not node:
                return 0
            if node.val>=maxVal:
                count=1
            else:
                count=0 
            maxVal=max(node.val,maxVal)
            count+= dfs(node.left,maxVal)
            count+=dfs(node.right,maxVal)
            return count 
        return dfs(root,root.val)

            