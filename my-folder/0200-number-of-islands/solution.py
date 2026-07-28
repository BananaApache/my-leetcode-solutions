class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # bfs(row, col): will run on only 1s and traverse until all those 1s are converted to 0

        rows, cols = len(grid), len(grid[0])

        def bfs(startRow, startCol):
            q = deque([ (startRow, startCol) ])
            grid[startRow][startCol] = "0"
            while q:
                row, col = q.popleft()

                for addRow, addCol in [ [0,1],[1,0],[-1,0],[0,-1] ]:
                    newRow, newCol = row + addRow, col + addCol
                    if (0 <= newRow and newRow < rows) and (0 <= newCol and newCol < cols) and grid[newRow][newCol] == "1":
                        grid[newRow][newCol] = "0"
                        q.append( (newRow, newCol) )
        
        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    result += 1

        return result

