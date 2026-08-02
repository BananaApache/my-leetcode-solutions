class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # bfs(row, col): traverses 1s only, updates to 0s, adds to some area, updates result at end
            
        rows, cols = len(grid), len(grid[0])
        result = 0
        
        def bfs(startRow, startCol):
            nonlocal result
            q = deque([ (startRow, startCol) ])
            grid[startRow][startCol] = 0
            area = 1

            while q:
                row, col = q.popleft()

                for addRow, addCol in [ [1,0],[0,1],[-1,0],[0,-1] ]:
                    newRow, newCol = row + addRow, col + addCol
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1:
                        q.append( (newRow, newCol) )
                        grid[newRow][newCol] = 0
                        area += 1
            
            result = max(result, area)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    bfs(row, col)
        
        return result


