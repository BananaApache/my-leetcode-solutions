class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # DP Solution

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = int(total / 2)

        possibleSums = set()
        possibleSums.add(0)

        for index in range(len(nums) - 1, -1, -1):
            newSums = set()
            for total in possibleSums:
                newSum = total + nums[index]
                if newSum == target:
                    return True
                elif newSum < target:
                    newSums.add(newSum)
            newSums.add(nums[index])

            possibleSums.update(newSums)

        return False

        # DFS backtracking decision tree solution

        # total = sum(nums)
        # if total % 2 != 0:
        #     return False

        # target = int(total / 2)

        # def dfs(startIndex, total):
        #     if total == target:
        #         return True
            
        #     for index in range(startIndex + 1, len(nums)):
        #         if dfs(index, total + nums[index]):
        #             return True

        #     return False

        # for index in range(len(nums)):
        #     if dfs(index, nums[index]):
        #         return True
        
        # return False
        

