class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        text1 = s
        text2 = s[::-1]

        # text1 rows
        # text2 cols
        dp = [ [0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1) ]

        for row in range(len(text1)-1, -1, -1):
            for col in range(len(text2)-1, -1, -1):
                if text1[row]==text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]

