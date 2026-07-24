# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # child need information current number from parent to append child value
        # dfs(node, curr): traversing down until leaf node adding to curr string
        # recurrence: check node is leaf, add to result, else traverse children

        result = 0

        def dfs(root, curr):
            nonlocal result
            # base case
            if not root:
                return
            
            curr = (curr * 10) + root.val
            if not root.left and not root.right:
                result += curr
            
            dfs(root.left, curr)
            dfs(root.right, curr)

            return
        
        dfs(root, 0)
        return result
