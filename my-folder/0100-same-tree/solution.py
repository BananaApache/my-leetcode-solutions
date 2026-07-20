# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # check current node
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            currentIsSame = p.val == q.val

        # recurisvely check left and right
        return currentIsSame and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

