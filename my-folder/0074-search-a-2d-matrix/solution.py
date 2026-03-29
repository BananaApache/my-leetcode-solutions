class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
        target 3

        [    0  1  2  3        
        0   [1, 3, 5, 7],    tcb  
        1   [10,11,16,20],    
        2   [23,30,34,60]]    
             l  m     r           
        """

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            center = (bottom + top) // 2
            start = matrix[center][0] # start
            end = matrix[center][-1] # end

            if start <= target and target <= end:
                # do binary search
                left = 0
                right = len(matrix[center]) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if matrix[center][middle] < target: # move left
                        left = middle + 1
                    elif matrix[center][middle] > target: # move right
                        right = middle - 1
                    else:
                        return True
                
                return False

            elif target > end:
                top = center + 1
            else:
                bottom = center - 1

        return False

