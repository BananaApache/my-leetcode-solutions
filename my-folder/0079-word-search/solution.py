class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        
        def backtrack(row, col, wordIndex, seen):
            # base case
            if board[row][col] != word[wordIndex]:
                return False
            if wordIndex == len(word) - 1:
                return True
            
            seen.add( (row, col) )
            for addRow, addCol in [ [1,0],[0,1],[-1,0],[0,-1] ]:
                newRow, newCol = row + addRow, col + addCol
                if newRow in range(rows) and newCol in range(cols) and (newRow, newCol) not in seen:
                    if backtrack(newRow, newCol, wordIndex + 1, seen):
                        return True
            
            seen.remove( (row, col) )
            return False
            
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    seen = set()
                    if backtrack(row, col, 0, seen):
                        return True

        return False

