class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def dfs(row):
            if row == n:
                result.append( ["".join(row) for row in board] )
                return
            
            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                dfs(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            
        dfs(0)
        return result
                

        # then loop through remaining rows and try to put a queen there
        # once placed a queen, eliminate the spots it blocks from the remaining board positions
        # try to place next queen
        # add back the spots once there are no more spots
        # if n = 0, append to result

        # result = []
        # board = ['.' * n] * n

        # def isGood(row, col):
        #     # col
        #     for index in range(n):
        #         if index != row and board[index][col] == 'Q':
        #             return False
        #     # diagonal
        #     for index in range(1, n):
        #         # check these
        #         # board[row - index][col - index]
        #         # board[row - index][col + index]
        #         # board[row + index][col + index]
        #         # board[row + index][col - index]
        #         for mRow, mCol in [ [1,1],[-1,1],[1,-1],[-1,-1] ]:
        #             checkRow, checkCol = row + mRow * index, col + mCol * index
        #             if 0<=checkRow<n and 0<=checkCol<n and board[checkRow][checkCol] == 'Q':
        #                 return False
        #     return True

        # def dfs(row):
        #     # base case
        #     if row >= n:
        #         result.append(board.copy())
        #         return
            
        #     for col in range(n):
        #         board[row] = board[row][ : col] + 'Q' + board[row][col + 1 : ]
        #         if isGood(row, col):
        #             dfs(row + 1)
        #         board[row] = board[row][ : col] + '.' + board[row][col + 1 : ]

        # dfs(0)
        # return result

