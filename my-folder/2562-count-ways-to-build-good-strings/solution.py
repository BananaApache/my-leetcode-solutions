class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        # topdown dfs with memo
        # dfs(currLength): ways to make good strings starting at currLength
        
        cache = {}
        def dfs(currLength):
            # base case
            if currLength > high:
                return 0
            if currLength in cache:
                return cache[currLength]
            
            total = 1 if low <= currLength else 0
            total += dfs(currLength + zero)
            total += dfs(currLength + one)
            cache[currLength] = total % (10**9 + 7)
            return cache[currLength]
        return dfs(0)

