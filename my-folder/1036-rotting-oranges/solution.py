class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # bfs(row, col): will traverse 4 directionally from a 2, converting 1s to 2s, updating minutes

        rows, cols = len(grid), len(grid[0])
        totalFresh = 0
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    totalFresh += 1
                elif grid[row][col] == 2:
                    q.append( (row, col, 0) )
        
        minutes = 0
        while q:
            row, col, time = q.popleft()

            for addRow, addCol in [ [1,0],[0,1],[-1,0],[0,-1] ]:
                newRow, newCol = row + addRow, col + addCol
                if (0<=newRow<rows and 0<=newCol<cols) and grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    totalFresh -= 1
                    q.append( (newRow, newCol, time + 1) )
            minutes = time
        
        if totalFresh > 0:
            return -1
        else:
            return minutes

