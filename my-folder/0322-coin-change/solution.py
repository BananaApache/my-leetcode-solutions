class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # target 7
        # [1,2,3,5]

        # START AT 1
        # [0,1,2,3,4,5,6,7] 
        # [8,1,1,1,2,8,8,8] dp

        for coin in range(1, amount + 1): # 1 BASED INDEXING FOR NOW
            for c in coins:
                if coin - c >= 0:
                    dp[coin] = min(dp[coin], 1 + dp[coin - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

