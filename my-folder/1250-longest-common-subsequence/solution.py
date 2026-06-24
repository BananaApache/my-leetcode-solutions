class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # TEXT1 is ROWS
        # TEXT2 is COLS
        rows = len(text1)
        cols = len(text2)

        dpRow = [0 for _ in range(cols + 1)]

        for row in range(rows - 1, -1, -1):
            newRow = [0 for _ in range(cols + 1)]
            for col in range(cols - 1, -1, -1):
                if text1[row] == text2[col]:
                    newRow[col] = 1 + dpRow[col + 1]
                else:
                    newRow[col] = max(newRow[col + 1], dpRow[col])
            dpRow = newRow
        
        return dpRow[0]

