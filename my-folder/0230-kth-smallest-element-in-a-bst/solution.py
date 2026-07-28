# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # dfs(node): traverses left - root - right ,incrementing index until gotten to k
        # should return True when found

        index = 0
        def dfs(root):
            nonlocal index

            # base case
            if not root:
                return False

            left = dfs(root.left)
            if left is not False:
                return left
            index += 1
            if index == k:
                return root.val
            right = dfs(root.right)
            if right is not False:
                return right
            return False
        
        return dfs(root)

