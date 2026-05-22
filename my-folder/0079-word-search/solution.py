class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxRow, maxCol = len(board), len(board[0])

        def backtrack(row, col, seen, index):
            if index == len(word):
                return True
            if (row < 0 or row >= maxRow or 
                col < 0 or col >= maxCol or
                (row, col) in seen or 
                board[row][col] != word[index]):
                return False
            
            seen.add((row, col))
            found = (backtrack(row - 1, col, seen, index + 1) or
                     backtrack(row + 1, col, seen, index + 1) or
                     backtrack(row, col - 1, seen, index + 1) or
                     backtrack(row, col + 1, seen, index + 1))
            seen.remove((row, col))
            return found

        positions = []

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    positions.append( (row, col) )

        for position in positions:
            row, col = position
            if backtrack(row, col, set(), 0):
                return True
        
        return False

