# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # minimum information is current index
        # dfs(root): while going back up, updates index and will return when k == index the correct node
        # left -> root -> right

        index = 0

        def dfs(root):
            nonlocal index
            # base case
            if not root:
                return None
            
            left = dfs(root.left)
            if left is not None:
                return left
            index += 1
            if index == k:
                return root.val
            right = dfs(root.right)
            if right is not None:
                return right

        return dfs(root)

