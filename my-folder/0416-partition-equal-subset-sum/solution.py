class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        # topdown with memoization
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        possibles = {0}

        for index in range(len(nums)):
            newPossibles = set()
            for possible in possibles:
                newPossible = possible + nums[index]
                if newPossible == target:
                    return True
                elif newPossible < target:
                    newPossibles.add( possible + nums[index] )
            possibles.update(newPossibles)
        
        return False

