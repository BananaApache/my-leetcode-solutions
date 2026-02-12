class Solution:
    def trap(self, height: List[int]) -> int:
        
        # edge cases
        # n = 1
        if len(height) == 1:
            return 0

        # totalWater = 4
        # tmpWater = 6
        # [2,1,0,1,3,2,1,2,1]
        #          1       2        

        # --- sliding window ---

        # running count of total water
        totalWater = 0
        totalWater2 = 0
        tmpWater = 0

        # column at right index has to be taller than column at left index to form water box
        # right index should always be moving

        left = 0
        for right in range(1, len(height)):

            # if we found a taller right index, stop the water
            if height[right] >= height[left]:
                left = right
                totalWater += tmpWater
                tmpWater = 0
            else:
                tmpWater += height[left] - height[right]

        # totalWater = 4
        # totalWater2 = 1
        # tmpWater2 = 0
        # [2,1,0,1,3,2,1,2,1]
        #          3              

        # check if tmpWater is 0
        if tmpWater > 0:
            left2 = len(height) - 1
            tmpWater2 = 0
            # try looping through backwards from end to left
            for right2 in range(len(height) - 2, left - 1, -1):
                if height[right2] >= height[left2]:
                    left2 = right2
                    totalWater2 += tmpWater2
                    tmpWater2 = 0
                else:
                    tmpWater2 += height[left2] - height[right2]
            
        return totalWater + totalWater2
            
