class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        
        # first idea is topdown DFS with memo
        # dfs(total): ways to sum up nums to target starting from total
        # cache[total]: stores dfs(total)

        cache = {}
        def dfs(total):
            # base case
            if total in cache:
                return cache[total]
            if total == target:
                return 1
            if total > target:
                return 0

            curr = 0
            for num in nums:
                curr += dfs(total + num)
            cache[total] = curr
            return curr
        return dfs(0)

