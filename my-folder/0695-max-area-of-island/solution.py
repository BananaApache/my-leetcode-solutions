class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        result = 0

        def getNeighbors(row, col):
            neighbors = []
            directions = [ (1,0), (0,1), (-1,0), (0,-1) ]
            for addRow, addCol in directions:
                newRow, newCol = row + addRow, col + addCol
                if newRow in range(rows) and newCol in range(cols):
                    neighbors.append( (newRow, newCol) )
            
            return neighbors

        def bfs(q):
            grid[q[0][0]][q[0][1]] = "X"
            area = 1

            while q:
                row, col = q.popleft()
                for newRow, newCol in getNeighbors(row, col):
                    if grid[newRow][newCol] == 1:
                        q.append( (newRow, newCol) )
                        grid[newRow][newCol] = "X"
                        area += 1
            
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = bfs(deque([(row, col)]))
                    result = max(result, area)

        return result
        

