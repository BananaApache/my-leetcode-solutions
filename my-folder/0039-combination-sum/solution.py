class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        # dfs and backtracking
        # append to current when going down
        # pop when going back up

        # decisions are the candidates at each level

        result = []

        #  0 1 2
        # [2,3,5]
        # target = 8


        def dfs(curr, total, index):
            # base case
            if total > target:
                return
            if total == target:
                result.append(curr.copy())
                return

            for newIndex in range(len(candidates[index : ])):
                curr.append(candidates[newIndex + index])
                dfs(curr, total + candidates[newIndex + index], index + newIndex)
                curr.pop()
        
        dfs([], 0, 0)
        # curr = []
        # for index in range(len(candidates)):
        #     curr.append(candidates[index])
        #     dfs(curr, candidates[index], index)
        #     curr.pop()
            
        return result

