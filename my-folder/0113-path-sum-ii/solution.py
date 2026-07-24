# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # child needs path information passed down from parent
        # node knows if it is leaf or not
        # dfs(node, runningSum, path): traverses down and keeps a total sum and the current path
        # recurrence: node checks if self is leaf then appends to result if runningSum is target, else traverse children

        result = []

        def dfs(root, runningSum, path):
            # base case
            if not root:
                return

            path.append(root.val)
            runningSum += root.val
            if not root.left and not root.right and runningSum == targetSum:
                result.append(path)
                return
            dfs(root.left, runningSum, path.copy())
            dfs(root.right, runningSum, path.copy())
            path.pop()

            return
        
        dfs(root, 0, [])
        return result

