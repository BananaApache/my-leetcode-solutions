class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # start from atlantic, add the heights you can reach to set
        # start from pacific , add the heights you can reach to set
        # return intersection of sets as list

        # working backward, queue entry will be row, col
        # enqueue if next height greater than or equal

        rows, cols = len(heights), len(heights[0])

        reachFromPacific = set()
        reachFromAtlantic = set()

        def bfs(startRow, startCol, reachSet):
            q = deque([ (startRow, startCol) ])
            if (startRow, startCol) in reachSet:
                return
            reachSet.add( (startRow, startCol) )

            while q:
                row, col = q.popleft()

                for addRow, addCol in [ [1,0],[-1,0],[0,1],[0,-1] ]:
                    newRow, newCol = row + addRow, col + addCol
                    if (0<=newRow<rows and 0<=newCol<cols) and heights[newRow][newCol] >= heights[row][col] and (newRow, newCol) not in reachSet:
                        q.append( (newRow, newCol) )
                        reachSet.add( (newRow, newCol) )

        # pacific
        for row in range(rows):
            bfs(row, 0, reachFromPacific)
        
        for col in range(cols):
            bfs(0, col, reachFromPacific)

        # atlantic
        for row in range(rows):
            bfs(row, cols - 1, reachFromAtlantic)
        
        for col in range(cols):
            bfs(rows - 1, col, reachFromAtlantic)

        return list( reachFromPacific & reachFromAtlantic )

