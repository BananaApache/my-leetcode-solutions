# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, bottom, top):
        # base case
        if root is None:
            return True

        if not (bottom < root.val and root.val < top):
            return False

        return self.dfs(root.left, bottom, min(root.val, top)) and self.dfs(root.right, max(root.val, bottom), top)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root, float("-inf"), float("inf"))
         

