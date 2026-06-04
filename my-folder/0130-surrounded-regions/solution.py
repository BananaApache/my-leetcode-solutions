class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        visited = set()

        def isEdge(row, col):
            return ((row == 0) or (row == rows - 1)) or ((col == 0) or (col == cols - 1))

        def bfs(startRow, startCol):
            q = deque([(startRow, startCol)])
            visited.add( (startRow, startCol) )

            while q:
                row, col = q.popleft()

                for addRow, addCol in [[1,0],[0,1],[-1,0],[0,-1]]:
                    newRow, newCol = row + addRow, col + addCol
                    if newRow in range(rows) and newCol in range(cols) and board[newRow][newCol] == 'O' and (newRow, newCol) not in visited:
                        q.append( (newRow, newCol) )
                        visited.add( (newRow, newCol) )

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and isEdge(row, col):
                    bfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited:
                    board[row][col] = 'X'

