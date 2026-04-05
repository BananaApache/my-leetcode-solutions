class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        diagonals = [] # set of tuples (row, column)

        """
        0
        mat = [
               [1,2,3],
               [4,5,6],
               [7,8,9]
              ]
        """

        for index in range(len(mat)):
            diagonal1 = (index, index)
            diagonal2 = (len(mat) - 1 - index, index)

            if diagonal1 != diagonal2:
                diagonals.append(diagonal1)
                diagonals.append(diagonal2)
            else:
                diagonals.append(diagonal1)

        result = 0
        for diagonal in diagonals:
            row, col = diagonal

            result += mat[row][col]
    
        return result

