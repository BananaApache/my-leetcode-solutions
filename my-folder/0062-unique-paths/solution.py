class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        # super complicated 2D DP :(

        row = [1] * n

        for _ in range(m - 1):
            newRow = [1] * n
            for index in range(n - 2, -1, -1):
                newRow[index] = newRow[index + 1] + row[index]
            row = newRow

        return row[0]

        # rows, cols = m, n

        # dp = [ [0 for _ in range(cols)] for _ in range(rows)]
        # dp[rows - 1][cols - 1] = 1

        # print(dp)

        # for row in range(rows - 1, -1, -1):
        #     for col in range(cols - 1, -1, -1):
        #         if row == rows - 1 and col == cols - 1:
        #             continue
                
        #         if row + 1 in range(rows):
        #             dp[row][col] += dp[row + 1][col]
        #         if col + 1 in range(cols):
        #             dp[row][col] += dp[row][col + 1]
        
        # return dp[0][0]



        # easy peasy combinatorics
        # n = (m + n - 2)
        # print(n)

        # return int((factorial(n)) / (factorial(m - 1) * factorial(n - m + 1)))

