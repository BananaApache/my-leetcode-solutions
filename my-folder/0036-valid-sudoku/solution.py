class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for rowIndex in range(0, 9):
            if not self.isValidRow(board, rowIndex):
                return False

        for columnIndex in range(0, 9):
            if not self.isValidColumn(board, columnIndex):
                return False

        if not self.isValidBox(board):
            return False

        return True
            
    def isValidRow(self, board, rowIndex):
        row = board[rowIndex]
        row = list(''.join(row).replace('.', ''))
        return len(set(row)) == len(row)

    def isValidColumn(self, board, columnIndex):
        column = []
        for rowIndex in range(0, 9):
            column.append(board[rowIndex][columnIndex])
    
        column = list(''.join(column).replace('.', ''))
        return len(set(column)) == len(column)

    def isValidBox(self, board):
        
        for row in range(0, 7, 3):
            for column in range(0, 7, 3):
                box = ''
                box += ''.join(board[row][column : column + 3])
                box += ''.join(board[row + 1][column : column + 3])
                box += ''.join(board[row + 2][column : column + 3])

                print(box)
                box = list(box.replace('.', ''))

                if len(set(box)) != len(box):
                    return False

        return True

                


