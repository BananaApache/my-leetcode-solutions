# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # NOTES
        # information needed from children!
        # children pass up their max path sum to parent, sounds like bottom up

        # but need to accumulate a max result since path doesnt need to go through root
        
        # a single node can also be a path too, so accumulate max before adding its children's max
        # a left or right child max could decrease, so take max of either or all

        # PLAN
        # state: just node
        # dfs(node): returns max path so far of node and below itself
        # recurrence: adjust max, get max from left and right, adjust max again from sum(left + right + node)

        # EXAMPLE
        # """
        # dfs 1, result 1
        # dfs 2, result 2
        # dfs 3, result 3 back up to dfs 1, result max(1 + 2 + 3, 1 + 2, 1 + 3, 3)
        # """

        # AFTER REALIZATION:
        # dfs(root): must return the biggest of one path but still set the result of max of left and/or right + root.val

        result = -float('inf')

        def dfs(root):
            nonlocal result
            # base case
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            biggest = max(root.val + max(left, right), root.val)
            result = max(root.val, left + root.val + right, left + root.val, root.val + right, result)

            return biggest

        dfs(root)
        return result

        # result = -float('inf')

        # def dfs(root):
        #     nonlocal result
        #     # base case
        #     if not root:
        #         return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)
            
        #     biggest = max(root.val, root.val + left + right, root.val + left, root.val + right)
        #     result = max(biggest, result)

        #     return biggest

        # dfs(root)
        # return result

        

