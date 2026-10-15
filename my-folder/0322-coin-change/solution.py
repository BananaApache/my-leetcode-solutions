class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        # bottomup tabular

        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for index in range(1, len(dp)):
            for coin in coins:
                target = index - coin
                if target >= 0:
                    dp[index] = min(dp[index], 1 + dp[target])
        return dp[amount] if dp[amount] != amount + 1 else -1

        # topdown with memoization
        # dfs(total): represents min number of coins needed to make up amount - total
        
        # cache = {}
        # def dfs(total):
        #     # base case
        #     if total > amount:
        #         cache[total] = amount + 1
        #         return amount + 1
        #     if total == amount:
        #         return 0
        #     if total in cache:
        #         return cache[total]

        #     ways = amount + 1
        #     for coin in coins:
        #         ways = min(ways, 1 + dfs(total + coin))
        #     cache[total] = ways
        #     return ways

        # ways = dfs(0)
        # if ways == amount + 1:
        #     return -1
        # else:
        #     return ways

