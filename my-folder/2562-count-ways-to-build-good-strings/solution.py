class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        # state: currLength
        # dfs(currLength): ways to build good strings from index to end
        # recurrence: add (1 if index in range[low, high]) + dfs(index + zero) + dfs(index + one)

        cache = {}

        def dfs(currLength):
            # base case
            if currLength > high:
                return 0
            if currLength in cache:
                return cache[currLength]
            
            numWays = 0

            if currLength in range(low, high + 1):
                numWays += 1

            numWays += dfs(currLength + zero) + dfs(currLength + one)
            cache[currLength] = numWays % (10**9 + 7)
            return numWays
        
        return dfs(0) % (10**9 + 7)

