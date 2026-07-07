class Solution:
    def numSquares(self, n: int) -> int:
        
        possibles = [num ** 2 for num in range(1, int(math.ceil(math.sqrt(n))) + 1 )]

        dp = [ n + 1 ] * (n + 1)
        dp[0] = 0

        for index in range(len(dp)):
            for possible in possibles:
                difference = index - possible
                if difference >= 0:
                    dp[index] = min(dp[index], 1 + dp[difference])
        
        return dp[n]

