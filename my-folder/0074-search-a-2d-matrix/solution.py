class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle = (bottom + top) // 2
            if matrix[middle][-1] < target:
                top = middle + 1
            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                break
        
        if not (top <= bottom):
            return False

        left = 0
        right = len(matrix[0]) - 1
        row = (top + bottom) // 2

        while left <= right:
            middle = (right + left) // 2
            if matrix[row][middle] < target:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        
        return False

