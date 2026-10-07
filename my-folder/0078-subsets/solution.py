class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # nums  1,2,3
        # index 1

        result = []

        def dfs(root, index):
            # base case
            if index == len(nums):
                result.append(root.copy())
                return

            root.append(nums[index])
            dfs(root, index + 1)
            root.pop()
            dfs(root, index + 1)

        dfs([], 0)

        return result

