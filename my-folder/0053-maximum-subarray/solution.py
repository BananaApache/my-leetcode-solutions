class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = nums[0]
        currentTotal = 0

        for right in range(len(nums)):
            currentTotal += nums[right]
            result = max(result, currentTotal)
            if currentTotal < 0:
                currentTotal = 0
        
        return result

