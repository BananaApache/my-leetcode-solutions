# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        # dfs(root) return height
        def dfs(root):
            nonlocal diameter
            # base case
            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            newHeight = 1 + max(leftHeight, rightHeight)
            diameter = max(leftHeight + rightHeight, diameter)
            return newHeight
        
        dfs(root)
        return diameter

