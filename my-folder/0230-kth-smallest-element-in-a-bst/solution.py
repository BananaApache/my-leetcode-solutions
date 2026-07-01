# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        answer = None
        count = k
        
        def dfs(root):
            nonlocal count, answer
            if root is None:
                # we are at an end
                return
            
            # keep going left
            dfs(root.left)
            # check root
            if count == 1:
                answer = root.val
            count -= 1
            # go right
            dfs(root.right)

        dfs(root)
        return answer

