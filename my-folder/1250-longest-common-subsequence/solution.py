class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # assuming length of text1 > text2
        # 2D DP dp[row][col] represents text2[row : ] subsequence from text1[col : ]
        # dp[0][0] will give answer
        # each cell is calculated : 1 + max(down, right) if text2[row]==text1[col] else 0 + max(down, right)

        smaller = text1
        bigger = text2
        
        # len(smaller) rows
        # len(bigger)  cols
        dp = [ [0 for _ in range(len(bigger) + 1)] for _ in range(len(smaller) + 1)]

        # start from bottom right, traverse right to left, down to up
        for row in range(len(smaller) - 1, -1, -1):
            for col in range(len(bigger) - 1, -1, -1):
                if smaller[row] == bigger[col]:
                    diagonal = dp[row + 1][col + 1]
                    dp[row][col] = 1 + diagonal
                else:
                    down = dp[row + 1][col]
                    right = dp[row][col + 1]
                    dp[row][col] = max(down, right)
        return dp[0][0]

