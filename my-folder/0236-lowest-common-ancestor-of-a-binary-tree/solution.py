# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # dfs(root): returns the lowest point at which we found p, q, LCA, or None

        def dfs(root):
            # base case
            if not root:
                return None
            if root.val == p.val:
                return p
            elif root.val == q.val:
                return q

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root

            elif left and not right:
                return left
            elif right and not left:
                return right

        return dfs(root)            


        # pPath = []
        # qPath = []

        # def dfs(root, path, target):
        #     # base case
        #     if not root:
        #         return False
        #     if root.val == target:
        #         path.append(root.val)
        #         return True
            
        #     path.append(root.val)
        #     if dfs(root.left, path, target):
        #         return True
        #     if dfs(root.right, path, target):
        #         return True

        #     path.pop()
        
        # dfs(root, pPath, p.val)
        # dfs(root, qPath, q.val)

        # return TreeNode(list(set(pPath) & set(qPath))[::-1][0])

