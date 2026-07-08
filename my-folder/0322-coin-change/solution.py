class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for index in range(len(dp)):
            for coin in coins:
                difference = index - coin
                if difference >= 0:
                    dp[index] = min(dp[index], 1 + dp[difference])

        print(dp)

        return dp[amount] if dp[amount] != amount + 1 else -1

