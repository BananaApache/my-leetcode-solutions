# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node = root

        lca = node
        found = False

        pAncestor = node
        qAncestor = node

        while not found:
            if p.val < pAncestor.val:
                pAncestor = pAncestor.left
            elif p.val > pAncestor.val:
                pAncestor = pAncestor.right
            else:
                found = True
                pAncestor = pAncestor

            if q.val < qAncestor.val:
                qAncestor = qAncestor.left
            elif q.val > qAncestor.val:
                qAncestor = qAncestor.right
            else:
                found = True
                qAncestor = qAncestor

            if (pAncestor and qAncestor) and (pAncestor.val == qAncestor.val):
                lca = pAncestor

        return lca

