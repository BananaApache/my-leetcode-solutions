# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # top down dfs
        # a child node needs to know the biggest so far

        result = 0
        biggest = -float('inf')
        def dfs(root, biggest):
            nonlocal result
            # base case
            if not root:
                return
            
            if root.val >= biggest:
                result += 1
            
            dfs(root.left, max(biggest, root.val))
            dfs(root.right, max(biggest, root.val))
            return
        
        dfs(root, biggest)
        return result

