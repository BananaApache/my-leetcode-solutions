class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # check total even
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = int(total / 2)

        possibles = {0}
        dp = [None] * len(nums)

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

