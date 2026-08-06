class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # dfs will work because exploring one path deeply
        # keep appending to current word until wrong letter then backtrack
        # run dfs only on cells with first letter of word
        # question is how to build seen set
        # use different seen set for each possible start because word can loop back around

        rows, cols = len(board), len(board[0])

        # traverses path until cell doesnt match the letter of word at index
        def dfs(index, row, col):
            # base case
            if index == len(word) - 1:
                if board[row][col] == word[index]:
                    return True
                else:
                    return False
            if board[row][col] != word[index]:
                return False
            
            # seen.add( (row, col) )
            board[row][col] = f"#bruh{board[row][col]}"
            for addRow, addCol in [ [1,0],[0,1],[-1,0],[0,-1] ]:
                newRow, newCol = row+addRow, col+addCol
                if 0<=newRow<rows and 0<=newCol<cols and not board[newRow][newCol].startswith("#"):
                    if dfs(index+1, newRow, newCol):
                        return True
            board[row][col] = board[row][col][5]
            return False
        
        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
        
        return False

