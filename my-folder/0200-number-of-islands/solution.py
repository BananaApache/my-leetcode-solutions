class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            q = deque()
            visited.add( (row, col) )
            q.append( (row, col) )

            while q:
                newRow, newCol = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    row, col = newRow + dr, newCol + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands

