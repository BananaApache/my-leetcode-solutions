class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])  

        def inP(row, col):
            return row == 0 or col == 0
        def inA(row, col):   
            return row == rows - 1 or col == cols - 1
        
        # bfs
        def canReachBoth(startRow, startCol):
            q = deque( [(startRow, startCol)] )
            visited = { (startRow, startCol) }

            reachedP = inP(startRow, startCol)
            reachedA = inA(startRow, startCol)

            if reachedP and reachedA:
                return True

            while q:
                row, col = q.popleft()

                for addRow, addCol in [[1,0],[0,1],[-1,0],[0,-1]]:
                    newRow, newCol = row+addRow, col+addCol
                    if newRow in range(rows) and newCol in range(cols) and (newRow, newCol) not in visited and heights[newRow][newCol] <= heights[row][col]:
                        reachedP = reachedP or inP(newRow, newCol)
                        reachedA = reachedA or inA(newRow, newCol)
                        if reachedP and reachedA:
                            return True

                        q.append( (newRow, newCol) )
                        visited.add( (newRow, newCol) )

            return reachedP and reachedA

        result = []
        for row in range(rows):
            for col in range(cols):
                if canReachBoth(row, col):
                    result.append( [row, col] )
        
        return result

