class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        # find rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rookRow, rookCol = i, j

        print(rookRow, rookCol)

        result = 0
        # top
        for row in range(rookRow, -1, -1):
            if board[row][rookCol] == 'B':
                break
            elif board[row][rookCol] == 'p':
                result += 1
                # print("top")
                break
        
        # right
        for col in range(rookCol, 8):
            if board[rookRow][col] == 'B':
                break
            elif board[rookRow][col] == 'p':
                result += 1
                # print("right")
                break
        
        # left
        for col in range(rookCol, -1, -1):
            if board[rookRow][col] == 'B':
                break
            elif board[rookRow][col] == 'p':
                result += 1
                # print("left")
                break
        
        # bottom 
        for row in range(rookRow, 8):
            if board[row][rookCol] == 'B':
                break
            elif board[row][rookCol] == 'p':
                result += 1
                # print("bottom")
                break
        
        return result

