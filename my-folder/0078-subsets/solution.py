class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # nums  1,2,3
        # index 1

        result = []

        def dfs(root, index):
            # base case
            if index == len(nums):
                result.append(root)
                return

            dfs(root + [nums[index]], index + 1)
            dfs(root, index + 1)

        dfs([], 0)

        return result

