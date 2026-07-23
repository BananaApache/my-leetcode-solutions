# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # information being passed down to children : new targetSum, current path
        # dfs(root, target, path): explore root to current node and check for target and add to path accordingly

        result = []

        def dfs(root, target, path):
            # base case
            if not root:
                return

            path.append(root.val)
            if not root.left and not root.right and root.val == target: # leaf node that is equal
                result.append(path.copy())
                path.pop()
                return
            
            dfs(root.left, target - root.val, path)
            dfs(root.right, target - root.val, path)
            path.pop()

            return
        
        dfs(root, targetSum, [])
        return result
        
