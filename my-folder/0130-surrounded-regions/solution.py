class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # start at borders
        # run dfs on the bordering 'O's and add each neighbor to border set

        bordering = set()
        rows, cols = len(board), len(board[0])
        def atBorder(row, col):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                return True
            else:
                return False

        q = deque()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and atBorder(row, col):
                    q.append( (row, col) )
                    bordering.add( (row, col) )
        print(q)
        
        while q:
            row, col = q.popleft()

            for addRow, addCol in [ [1,0],[0,1],[-1,0],[0,-1] ]:
                newRow, newCol = row+addRow, col+addCol
                if 0<=newRow<rows and 0<=newCol<cols and board[newRow][newCol] == 'O' and (newRow, newCol) not in bordering:
                    q.append( (newRow, newCol) )
                    bordering.add( (newRow, newCol) )
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in bordering:
                    board[row][col] = 'X'

