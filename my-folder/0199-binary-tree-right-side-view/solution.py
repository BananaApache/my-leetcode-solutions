# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        # dfs(root, index): top down traversal, setting each index of result and overriding if more to the right

        def dfs(root, index):
            # base case
            if not root:
                return

            if index == len(result):
                result.append(root.val)
            elif index < len(result):
                result[index] = root.val
            
            dfs(root.left, index + 1)
            dfs(root.right, index + 1)

            return
        
        dfs(root, 0)
        return result

