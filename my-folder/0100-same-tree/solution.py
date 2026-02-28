# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # p -> root1
        # q -> root2

        # base case
        if (p is None) and (q is None): # both dont exist
            return True

        if p and q: # both exist
            rootIsSame = (p.val == q.val)
        else: # one doesnt exist
            rootIsSame = False

        return rootIsSame and (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

