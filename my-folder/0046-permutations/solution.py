
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(permutation, remaining):
            # base case
            if len(permutation) == len(nums):
                result.append(permutation)
                return

            for index in range(len(remaining)):
                dfs(permutation + [remaining[index]], remaining[:index] + remaining[index + 1:])

        for index in range(len(nums)):
            dfs([nums[index]], nums[:index] + nums[index + 1:])
        
        return result

