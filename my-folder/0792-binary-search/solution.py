class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # [-1,0,3,5,9,12]  length 6, target 9
        #   0 1 2 3 4 5 

        # [9,12]    length 2, target 9
        #  0 1

        # medianIndex = 6 // 2 = 3
        # nums[medianIndex] = 5

        # get the median
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = int((left + right) / 2)

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1

