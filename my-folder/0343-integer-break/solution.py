class Solution:
    def integerBreak(self, n: int) -> int:
        
        # 1d dp
        # dp[number]: max product of number
        # dp[number] = max( dp[n1] + dp[n2] ), where n1 + n2 = number
        # n1, n2 < number // 2

        if n < 5:
            return {2:1,3:2,4:4}[n]

        dp = [1] * (n + 1)
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for index in range(5, len(dp)):
            left = 1
            right = index - 1
            candidate = 1
            while left <= right:
                candidate = max(candidate, dp[left] * dp[right])
                left += 1
                right -= 1
            dp[index] = candidate
        return dp[n]

