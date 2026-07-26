# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # pre: root, LEFT, RIGHT
        # in : LEFT, root, RIGHT

        # first in pre -> ROOT
        # in: [left .. root .. right]
        # size of left for inorder list and size of right for inorder list is useful information
        # pre: [root .. size of left .. size of right]

        #             0 1 2 3 4 5
        #             m             
        # preorder = [3,9,20,15,7]
        # inorder  = [9,3,15,20,7]
        #             L m

        inorderMap = {}
        for index in range(len(inorder)):
            inorderMap[inorder[index]] = index

        def build(preL, preR, inL, inR):
            # base case
            if preL == preR:
                return None
            if preR - preL == 1:
                return TreeNode(preorder[preL])

            root = TreeNode(preorder[preL])
            rootIndex = inorderMap[preorder[preL]]

            leftSize = rootIndex - inL
            rightSize = inR - rootIndex

            root.left = build( preL=preL + 1, preR=preL + leftSize + 1, inL=inL, inR=rootIndex )
            root.right = build( preL=preL + leftSize + 1, preR=preR, inL=rootIndex + 1, inR=inR)
            # root.left = build( preorder[ 1 : rootIndex + 1] , inorder[ 0 : rootIndex ] )
            # root.right = build( preorder[ rootIndex + 1 : ] , inorder[ rootIndex + 1 : ] )

            return root

        return build(0, len(preorder), 0, len(preorder))

