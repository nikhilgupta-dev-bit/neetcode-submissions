# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        # left root right 
        # approch inorder because it will give u in the form of sorted array then we can return kth smallest 
        def inorder(node):
            if not node :
                return 
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        return arr[k-1]
        # 1 index based 



            