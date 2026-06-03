class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        q = deque()
        totalOranges = 0
        rottens = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rottens.append( (row, col) )
                elif grid[row][col] == 1:
                    totalOranges += 1
        
        q.append(rottens)
        result = -1

        # bfs
        while q:
            rottens = q.popleft()
            result += 1
            newRottens = []
            for row, col in rottens:
                for addRow, addCol in [[1,0],[0,1],[-1,0],[0,-1]]:
                    newRow, newCol = row + addRow, col + addCol
                    if newRow in range(rows) and newCol in range(cols) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        totalOranges -= 1
                        newRottens.append( (newRow, newCol) )

            if newRottens:
                q.append(newRottens)
        
        if totalOranges > 0:
            return -1
        else:
            return result

