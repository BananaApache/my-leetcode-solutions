# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # base case
        if root and (root.left is None and root.right is None): # either left not exist or right not exist
            tmp = root.left
            root.left = root.right
            root.right = tmp
            return root

        # non base case
        if root:
            tmpTree = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
            root.left = tmpTree

        return root


