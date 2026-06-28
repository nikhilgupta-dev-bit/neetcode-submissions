# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inoder 
        #left root right
        prev=[float("-inf")]
        return self.valid(root,prev)
    def valid(self,node,prev):
        if not node :
            return True
        if not self.valid(node.left,prev):
            return False 
        if prev[0]>=node.val:
            return False 
        prev[0]=node.val
        return self.valid(node.right,prev)

        

        