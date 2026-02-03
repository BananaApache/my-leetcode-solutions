class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # initialize dp array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for target in range(1, len(dp)):
            for coin in coins:
                if target - coin >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1


