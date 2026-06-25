class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        
        nums = [num**2 for num in range(1, int(sqrt(n)) + 1)]

        for index in range(1, len(dp)):
            for num in nums:
                difference = index - num
                if difference >= 0:
                    dp[index] = min(dp[index], 1 + dp[difference])

        return dp[n]

