# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # SECOND ATTEMPT

        # preSums can be a frequency map

        result = 0

        def dfs(root, preSum, prefixMap):
            nonlocal result
            # base case
            if not root:
                return

            preSum += root.val
            
            result += prefixMap.get(preSum - targetSum, 0) # frequency of the num we need
            prefixMap[preSum] = prefixMap.get(preSum, 0) + 1
            dfs(root.left, preSum, prefixMap)
            dfs(root.right, preSum, prefixMap)
            prefixMap[preSum] = prefixMap.get(preSum, 0) - 1

            return
        
        dfs(root, 0, {0 : 1})
        return result
        
        # giving children a current path can be useful
        # this current path can be a list of sums before it
        # dfs(node, preSums): traversing down carrying a list of previous Sums and testing if current node added to any sum equals target
        # recurrence: add current node to all preSums and see if equals target, then update preSum path with that new sum

        # result = 0

        # def dfs(root, preSums):
        #     nonlocal result

        #     # base case
        #     if not root:
        #         return
            
        #     for index in range(len(preSums)):
        #         newSum = preSums[index] + root.val
        #         if newSum == targetSum:
        #             result += 1

        #         preSums[index] = newSum
        #     preSums.append(0)

        #     dfs(root.left, preSums.copy())
        #     dfs(root.right, preSums.copy())

        #     return
        
        # dfs(root, [0])
        # return result

