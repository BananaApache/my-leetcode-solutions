class Solution:
    def maxArea(self, height: List[int]) -> int:

        # [4, 3, 2, 7, 4, 9] len 6
        #  0  1  2  3  4  5               
        
        # initialize maxArea
        maxArea = 0

        # initialize left column and right column
        leftColumn = 0
        rightColumn = len(height) - 1

        # keep looping until left < right
        while leftColumn < rightColumn:
            # now find that shorter column
            shorterColumn = min(height[leftColumn], height[rightColumn])

            # calculate area, adjust new max
            maxArea = max(shorterColumn * (rightColumn - leftColumn), maxArea)

            # if left column shorter, move left ...
            # if both are equal, move left one
            # move the shorter column until you find a column thats taller or equal
            if height[leftColumn] <= height[rightColumn]:
                # keep moving pointer
                leftColumn += 1
                while height[leftColumn] <= shorterColumn and leftColumn < rightColumn:
                    leftColumn += 1
                    # set that shorter column height to this new one
            else:
                rightColumn -= 1
                while height[rightColumn] <= shorterColumn and leftColumn < rightColumn:
                    rightColumn -= 1


        # return maxArea
        return maxArea

