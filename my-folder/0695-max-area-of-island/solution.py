class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # dfs(row, col): traverses 1s, sets them to 0s, returns its area

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            # base case
            if not (0 <= row < rows and 0 <= col < cols):
                return 0
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            
            return 1 + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row - 1, col) + dfs(row, col - 1)

        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result = max(result, dfs(row, col))
            
        return result

