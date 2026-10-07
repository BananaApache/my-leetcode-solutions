class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # dfs will take a current permutation and add to from the remaining

        result = []

        def dfs(curr, remaining):
            # base case
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            
            for index in range(len(remaining)):
                curr.append(remaining[index])
                dfs(curr, remaining[:index]+remaining[index+1:])
                curr.pop()
            return
        
        dfs([], nums)
        return result
