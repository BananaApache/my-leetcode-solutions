class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        # run bfs on all pacific corners and atlantic corners
        # add to corresponding seen after traversed that node

        rows, cols = len(heights), len(heights[0])

        touchPacific = set()
        touchAtlantic = set()

        def bfs(startRow, startCol, seen):
            if (startRow, startCol) in seen:
                return
            q = deque([(startRow, startCol)])
            seen.add((startRow, startCol))
            while q:
                row, col = q.popleft()
                for addRow, addCol in [[0,1],[1,0],[0,-1],[-1,0]]:
                    newRow, newCol = row+addRow, col+addCol
                    if newRow in range(rows) and newCol in range(cols) and (newRow, newCol) not in seen and heights[newRow][newCol] >= heights[row][col]:
                        q.append( (newRow, newCol) )
                        seen.add((newRow, newCol))
        
        # pacific
        for row in range(rows):
            bfs(row, 0, touchPacific)
        for col in range(cols):
            bfs(0, col, touchPacific)

        # atlantic
        for row in range(rows):
            bfs(row, cols - 1, touchAtlantic)
        for col in range(cols):
            bfs(rows - 1, col, touchAtlantic)

        result = []
        for row, col in touchPacific:
            if (row, col) in touchAtlantic:
                result.append([row, col])
        return result
