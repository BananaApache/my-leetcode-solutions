class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        result = 0
        
        def bfs(startRow, startCol):
            q = deque( [(startRow, startCol)] )
            grid[startRow][startCol] = "0"

            while q:
                row, col = q.popleft()

                for addRow, addCol in [ [1,0],[0,1],[-1,0],[0,-1] ]:
                    newRow, newCol = row + addRow, col + addCol

                    if (newRow in range(rows) and newCol in range(cols)) and (grid[newRow][newCol] == "1"):
                        q.append( (newRow, newCol) )
                        grid[newRow][newCol] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    result += 1
                    bfs(row, col)

        return result

