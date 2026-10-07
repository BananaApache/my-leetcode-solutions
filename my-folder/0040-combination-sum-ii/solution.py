class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        # cut duplicate path starts at same level of decision tree
        # use index to keep track of current start

        result = []
        curr = []
        total = 0
        candidates.sort()

        def dfs(index):
            nonlocal total
            # base case
            if total > target:
                return
            if total == target:
                result.append(curr.copy())
                return
            
            for newIndex in range(index, len(candidates)):
                if newIndex != index and candidates[newIndex - 1] == candidates[newIndex]:
                    continue

                curr.append(candidates[newIndex])
                total += candidates[newIndex]
                dfs(newIndex + 1)
                curr.pop()
                total -= candidates[newIndex]

        dfs(0)
        return result

