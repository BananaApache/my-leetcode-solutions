# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    from collections import deque

    def isSameTree(self, p, q):
        # base case
        if not p and not q:
            return True

        if p and q:
            return (p.val == q.val) and (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # q = deque([root])
        q = [root]

        while q:
            node = q.pop()

            if node:
                if self.isSameTree(node, subRoot):
                    return True

                q.append(node.left)
                q.append(node.right)

        return False

