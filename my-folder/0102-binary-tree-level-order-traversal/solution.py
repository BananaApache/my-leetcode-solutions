# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []

        def dfs(root, index):
            # base case
            if not root:
                return
            
            if index == len(result):
                result.append( [root.val] )
            else:
                result[index].append(root.val)
            
            dfs(root.left, index + 1)
            dfs(root.right, index + 1)
        
        dfs(root, 0)

        return result

