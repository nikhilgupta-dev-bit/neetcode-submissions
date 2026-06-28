# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # this is a dfs problem 
        if not root :
            return None
        if key>root.val:
            # move to the right 
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            # serch in the left 
            root.left=self.deleteNode(root.left,key)
        else:
            # case 1 left screwed 
            if not root.left:
                return root.right 
            # case 2 right screwed
            if not root.right:
                return root.left 
            # case 3 if it consists of children nodes 
            # find the inorder succesor 
            curr=root.right 
            while curr.left :
                curr=curr.left
            root.val=curr.val
            root.right=self.deleteNode(root.right,curr.val)
        return root 
