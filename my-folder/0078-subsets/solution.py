class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        subset = []
        def dfs(index):
            # base case
            if index >= len(nums): # index out of bounds
                result.append(subset.copy())
                return

            # decision of adding nums[index]
            subset.append(nums[index])
            # then run dfs on next index
            dfs(index + 1)

            # decision of not adding nums[index]
            subset.pop()
            # then run dfs on next index
            dfs(index + 1)
        
        dfs(0)
        return result

