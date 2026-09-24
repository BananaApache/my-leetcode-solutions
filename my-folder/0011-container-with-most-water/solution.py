class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        result = 0
        left = 0
        right = len(height) - 1
        
        #  0 1 2 3 4 5 6 7 8     len 9
        # [1,8,6,2,5,4,8,3,7]
        #      1       2    
        # result 49         

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(area, result)

            # left smaller
            if height[left] <= height[right]:
                left += 1
            # right smaller
            else:
                right -= 1

        return result

