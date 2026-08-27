# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        # parent needs path length from child
        # dfs returns minimum path from leaf node to root of either left or right
        # bottom up
        # base case is leaf node

        def dfs(root):
            # base case
            if not root:
                return float('inf')
            if root and not root.left and not root.right:
                return 1
            
            # traverse
            leftPath = float('inf')
            rightPath = float('inf')
            if root:
                leftPath = dfs(root.left)
                rightPath = dfs(root.right)
            
            return 1 + min(leftPath, rightPath)
        
        return dfs(root)

