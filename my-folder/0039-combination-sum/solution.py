class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(total, path, index):
            if total == target:
                result.append(path)
                return
            if index >= len(candidates) or total > target:
                return

            dfs(total + candidates[index], path + [candidates[index]], index)
            dfs(total, path, index + 1)

        dfs(0, [], 0)

        return result

