# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # self.nums = []

        # def traverse(root):
        #     # base case
        #     if not root:
        #         return

        #     traverse(root.left)
        #     self.nums.append(root.val)
        #     traverse(root.right)

        #     return

        # traverse(root)

        # return self.nums[k - 1]

        # stack = [3,

        stack = []
        count = 0
        curr = root

        while curr or root:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right

