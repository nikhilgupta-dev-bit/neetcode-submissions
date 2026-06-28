# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        
        # check current node OR go left OR go right
        return (self.isSame(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return (p.val == q.val and
                self.isSame(p.left, q.left) and
                self.isSame(p.right, q.right))