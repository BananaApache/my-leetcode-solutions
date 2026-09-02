# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # preorder : ROOT, LEFT , RIGHT
        # postorder: LEFT, RIGHT, ROOT

        # root always first in pre
        # left is after root in pre

        # base case
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = preorder[0]
        rootNode = TreeNode(root)
        left = preorder[1]
        leftIndex = postorder.index(left)

        rootNode.left = self.constructFromPrePost(preorder[1:1+leftIndex+1], postorder[:leftIndex+1])
        rootNode.right = self.constructFromPrePost(preorder[1+leftIndex+1:], postorder[leftIndex+1:])
        return rootNode

