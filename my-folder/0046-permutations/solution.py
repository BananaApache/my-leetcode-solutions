class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # dfs will take a current permutation and add to from the remaining

        result = []

        def dfs(curr, remaining):
            # base case
            if len(curr) == len(nums):
                result.append(curr)
                return
            
            for index in range(len(remaining)):
                dfs(curr + [remaining[index]], remaining[:index]+remaining[index+1:])
            return
        
        for index in range(len(nums)):
            dfs([nums[index]], nums[:index]+nums[index+1:])
        return result
