# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # inorder: left - root - right
        # postorder: left - right - root
        # for postorder, root always at end of subarray

        # base case
        if not postorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])

        root = TreeNode(postorder[-1])
        rootIndex = inorder.index(postorder[-1])

        root.left = self.buildTree( inorder[ : rootIndex ], postorder[ : rootIndex ] )
        root.right = self.buildTree( inorder[ rootIndex + 1 : ], postorder[ rootIndex : -1 ] )

        return root

