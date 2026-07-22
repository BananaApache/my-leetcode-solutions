# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # recurrence: compare root against p and q, then compare p and q against right and left if needed
        # p,q < root: search left
        # p,q > root: search right
        # p < root < q OR p == root OR q == root: return root

        smaller = min(p.val, q.val)
        bigger = max(p.val, q.val)

        if (smaller <= root.val and root.val <= bigger):
            return root
        
        if bigger < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < smaller:
            return self.lowestCommonAncestor(root.right, p, q)

