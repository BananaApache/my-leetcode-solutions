class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # maybe sorted
        # no two pointers
        # sum NEEDS to be even
        
        # find if subset length (n - 1) can total to (sum / 2)

        # BRUTE FORCE IS DFS WITH BACKTRACK 2^(n-1)

        # DP -> sum of all subsets up to index

        numsTotal = sum(nums)
        if numsTotal % 2 != 0: # odd sum
            return False
        halfTotal = numsTotal // 2

        possibleTotals = {0}

        for num in nums:
            nextPossible = set()
            for total in possibleTotals:
                newTotal = total + num
                if newTotal == halfTotal:
                    return True
                elif newTotal < halfTotal:
                    nextPossible.add(newTotal)

            possibleTotals.update(nextPossible)

        return False

