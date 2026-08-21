class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # two pointers
        # left at start, right at end
        # keep moving shorter one
        # updating max

        def getArea(left, right):
            return min(height[left], height[right]) * (right - left)

        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            shorter = min(height[left], height[right])
            result = max(result, getArea(left, right))

            if height[left] <= height[right]:
                while left < right and height[left] <= shorter:
                    left += 1
            else:
                while left < right and height[right] <= shorter:
                    right -= 1
        
        return result
