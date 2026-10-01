# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        
        def dfs(node1, node2):
            # base cases
            if node1 and not node2:
                return node1
            elif not node1 and node2:
                return node2
            elif not node1 and not node2:
                return None
            
            # now they are both TreeNodes
            curr = TreeNode(node1.val + node2.val)
            curr.left = dfs(node1.left, node2.left)
            curr.right = dfs(node1.right, node2.right)
            return curr

        return dfs(root1, root2)

