# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        # Definition for a binary tree node.
        
        # do inorder traversal and keep track of previous

        result = float('inf')
        prev = None
        def dfs(root):
            nonlocal result, prev
            # base case
            if not root:
                return
            
            dfs(root.left)
            if prev:
                result = min(result, abs(prev.val - root.val))
            prev = root
            dfs(root.right)
            return
        dfs(root)
        return result
