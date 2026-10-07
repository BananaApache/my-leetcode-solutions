class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        # paths are remaining nums
        # skip a start path if its same as previous
        # always append to result
        # find a way to cut off duplicate branches

        result = []
        curr = []
        nums.sort()

        def dfs(index):
            result.append(curr.copy())
            # base case
            if index == len(nums):
                return
                

            for newIndex in range(index, len(nums)):
                if newIndex > index and nums[newIndex - 1] == nums[newIndex]:
                    continue
                
                curr.append(nums[newIndex])
                dfs(newIndex + 1)
                curr.pop()
        
        dfs(0)
        return result
