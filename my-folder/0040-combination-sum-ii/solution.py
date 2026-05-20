class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        result = []

        def dfs(total, path, index):
            # base case
            if total == target:
                result.append(path[:])
                return
            elif total > target or index == len(candidates):
                return
            
            path.append(candidates[index])
            dfs(total + candidates[index], path, index + 1)
            path.pop()

            curr = candidates[index]
            while not (index >= len(candidates) or curr != candidates[index]):
                index += 1
            dfs(total, path, index)

        dfs(0, [], 0)

        return result

