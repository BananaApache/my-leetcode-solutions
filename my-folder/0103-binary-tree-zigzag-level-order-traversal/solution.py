# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        if not root:
            return []

        result = []
        q = deque([ [root] ])
        while q:
            level = q.popleft()
            newLevel = []
            for index in range(len(level)):
                if level[index].left:
                    newLevel.append(level[index].left)
                if level[index].right:
                    newLevel.append(level[index].right)
                level[index] = level[index].val

            result.append(level)
            if newLevel:
                q.append(newLevel)
        
        for index in range(len(result)):
            if index % 2 != 0:
                result[index] = result[index][::-1]
        return result

