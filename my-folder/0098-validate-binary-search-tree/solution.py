# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, left, right):
            # base case
            if root is None:
                return True

            # print(f"{left} < {root.val} < {right}")

            return (left < root.val and root.val < right) and isValid(root.left, left, root.val) and isValid(root.right, root.val, right)
        
        return isValid(root.left, -float('inf'), root.val) and isValid(root.right, root.val, float('inf'))

