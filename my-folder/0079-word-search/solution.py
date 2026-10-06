class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # sounds like backtracking because we need to explore possibilities until current is wrong
        # can be implemented with DFS
        # need to have seen set too in case of cycle
        # DFS can track index
        # DFS checks whether at each index the current word is currect at the [row][col]

        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(index, row, col):
            # base cases
            if not (0<=row<rows and 0<=col<cols): # out of range of board
                return False
            if board[row][col] != word[index]: # current letter is wrong
                return False
            if (row, col) in seen: # did a loop
                return False
            if index == len(word) - 1: # reached end of word
                return True

            seen.add( (row, col) )
            for addRow, addCol in [ [1,0],[0,1],[-1,0],[0,-1] ]:
                if dfs(index + 1, row+addRow, col+addCol):
                    return True
            seen.remove( (row, col) )

            return False
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(0, row, col):
                    return True
        return False

