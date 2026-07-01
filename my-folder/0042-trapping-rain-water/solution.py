class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        left = 0
        tmpWater = 0

        for right in range(len(height)):
            if height[left] <= height[right]:
                total += tmpWater
                tmpWater = 0
                left = right
            else:
                tmpWater += height[left] - height[right]
        
        if tmpWater <= 0:
            return total
        
        stopped = left
        right = len(height) - 1
        tmpWater = 0
        for left in range(len(height) - 1, stopped - 1, -1):
            if height[right] <= height[left]:
                total += tmpWater
                tmpWater = 0
                right = left
            else:
                tmpWater += height[right] - height[left]

        return total

