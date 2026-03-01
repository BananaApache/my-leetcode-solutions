# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result = 0
        stack = [(root, root.val)]

        while stack:
            node, maxVal = stack.pop()

            if node:
                if node.val >= maxVal:
                    result += 1
                    maxVal = node.val

                stack.append( (node.left, maxVal) )
                stack.append( (node.right, maxVal) )

        return result

