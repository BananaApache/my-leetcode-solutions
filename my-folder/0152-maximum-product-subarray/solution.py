class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        currentMin = 1
        currentMax = 1
        result = max(nums)

        for index in range(len(nums)):
            if nums[index] == 0:
                currentMin = 1
                currentMax = 1
                continue

            new = nums[index] * currentMax
            currentMax = max(new, nums[index] * currentMin, nums[index])
            currentMin = min(new, nums[index] * currentMin, nums[index])
            result = max(result, currentMax)
        
        return result

