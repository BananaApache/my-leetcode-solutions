class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # use dfs to fully traverse a '1'

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            # base case
            if not (0<=row<rows and 0<=col<cols):
                return

            if grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return

        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    result += 1
        return result


