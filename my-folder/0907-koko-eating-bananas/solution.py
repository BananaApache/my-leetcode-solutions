class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        import math

        left = 1
        right = max(piles)
        result = right

        def canEat(speed):
            nonlocal result
            hours = 0

            for bananas in piles:
                hours += math.ceil(bananas / speed)
                        
            if hours <= h:
                return True
            else:
                return False
        

        while left <= right:
            speed = (left + right) // 2

            if canEat(speed):
                result = min(result, speed)
                right = speed - 1
            else:
                left = speed + 1

        return result

