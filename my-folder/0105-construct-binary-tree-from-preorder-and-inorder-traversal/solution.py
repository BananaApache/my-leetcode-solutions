# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder, inorder):
            # base case
            if len(preorder) == 0: 
                return None

            root = TreeNode(preorder[0])
            rootIndex = inorder.index(preorder[0])
            left = preorder[1 : rootIndex + 1]
            right = preorder[rootIndex + 1 : ]

            root.left = build(left, inorder[:rootIndex])
            root.right = build(right, inorder[rootIndex + 1:])

            return root

        return build(preorder, inorder)

        # root = preorder[0]
        # get the index of root from inorderSet
        # items in left subtree are 0..index
        # items in right subtree are index..len(inorder)




