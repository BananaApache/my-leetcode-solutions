# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def getDiameter(root: Optional[TreeNode]) -> int:
            global result
            # base case
            if not root:
                return 0

            left = getDiameter(root.left)
            right = getDiameter(root.right)

            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        # longest depth of left + longest depth of right

        getDiameter(root)

        return  self.result


