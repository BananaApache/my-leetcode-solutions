# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, left, right):
            if root is None:
                return True

            currIsValid = (left < root.val) and (root.val < right)
            if not currIsValid:
                return False
            else:
                return isValid(root.left, left, root.val) and isValid(root.right, root.val, right)

        return isValid(root, -math.inf, math.inf)

