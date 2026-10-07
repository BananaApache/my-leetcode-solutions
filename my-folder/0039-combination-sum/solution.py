class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        # paths are the remaining candidates
        # traverse decision tree until current sum is bigger than target or equal
        # pass in index to dfs to not traverse over previous to avoid duplicates

        result = []
        curr = []
        total = 0

        def dfs(index, remaining):
            if remaining == 0:
                result.append(curr.copy())
                return
            if remaining < 0:
                return

            for i in range(index, len(candidates)):
                curr.append(candidates[i])
                dfs(i, remaining - candidates[i])
                curr.pop()
            
        dfs(0, target)
        return result

