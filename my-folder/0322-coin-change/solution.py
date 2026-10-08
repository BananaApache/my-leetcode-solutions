class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)

        for index in range(len(dp)):
            if index == 0:
                dp[index] = 0
                continue

            for coin in coins:
                if coin <= index:
                    dp[index] = min(dp[index - coin] + 1, dp[index])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
