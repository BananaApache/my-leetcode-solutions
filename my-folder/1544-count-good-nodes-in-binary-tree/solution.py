# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # child needs max value so far from parent
        # dfs(root, maximum): traversing down and comparing value to maximum
        # recurrence: update result if current is greater than or equal to maximum, update new max, traverse children

        result = 0

        def dfs(root, maximum):
            nonlocal result
            # base case
            if not root:
                return
            
            # compare 
            if root.val >= maximum:
                result += 1
                maximum = root.val
            dfs(root.left, maximum)
            dfs(root.right, maximum)

            return
        
        dfs(root, -float('inf'))
        return result

