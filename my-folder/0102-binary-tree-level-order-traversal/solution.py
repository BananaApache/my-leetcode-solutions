# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        from collections import deque

        result = [[root.val]]
        level = []
        q = deque([root])
        tmpQ = deque()

        while q:
            node = q.popleft()

            if node:
                l = [node.left.val] if node.left else []
                r = [node.right.val] if node.right else []

                if l or r:
                    level += l + r

                tmpQ.append(node.left)
                tmpQ.append(node.right)

            if not q:
                q = tmpQ
                tmpQ = deque()
                if level:
                    result.append(level)
                level = []

        return result

