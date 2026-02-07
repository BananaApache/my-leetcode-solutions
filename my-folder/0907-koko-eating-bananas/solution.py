class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        
        # edge case
        # if length of piles equals h
        # biggest = max(piles)
        # if len(piles) == h:
        #     return biggest

        result = max(piles) + 1

        # piles = sorted(piles)[::-1]

        leftK = 1
        rightK = result - 1
        while leftK <= rightK:
            middleK = (leftK + rightK) // 2
            totalHours = 0

            for bananas in piles:
                totalHours += math.ceil(bananas / middleK)
                if totalHours > h:
                    # increase banana eating speed
                    leftK = middleK + 1
                    break
            
            if totalHours <= h:
                result = min(result, middleK)
                rightK = middleK - 1 # decrease banana eating speed

        return result



