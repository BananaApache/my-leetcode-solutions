class Solution:
    def climbStairs(self, n: int) -> int:
        
        dpArray = [0] * n

        def dfs(steps):
            # base cases
            if steps < n and dpArray[steps]:
                return dpArray[steps]
            if steps == n:
                return 1
            elif steps > n:
                return 0

            dpArray[steps] = dfs(steps + 1) + dfs(steps + 2)
            return dpArray[steps]

        return dfs(0)

