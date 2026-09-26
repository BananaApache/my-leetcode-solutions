class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        # want the heights in increasing order
        # each pillar can keep extending area to the right

        result = 0
        stack = [] # (index, height)

        # loop through heights
        for index in range(len(heights)):
            poppedIndex = index
            # while stack invalid
            while stack and heights[index] < stack[-1][1]:
                # pop from the stack
                poppedIndex, poppedHeight = stack.pop()
                # set new result
                result = max(result, (index - poppedIndex) * poppedHeight)
            # append to stack
            stack.append( (poppedIndex, heights[index]) )
        for poppedIndex, poppedHeight in stack:
            result = max(result, (len(heights) - poppedIndex) * poppedHeight)
        return result

