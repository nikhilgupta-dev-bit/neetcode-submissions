# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index=0 
        mpp={v:i for i,v in enumerate(inorder)}# set index store karaga both list pe 
        def dfs(l,r):
            nonlocal pre_index
            if l>r:
                return None 
            root_index=preorder[pre_index]
            root=TreeNode(root_index)
            # left subtree 
            pre_index+=1
            # 0 toh root ho gya 
            mid=mpp[root_index]
            # mid toh actually root hian 
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root 
        return dfs(0,len(inorder)-1)

        