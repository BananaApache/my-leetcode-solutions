class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #            max      min
        # maxMins = [ (nums[0], nums[0]) ]
        result = max(nums)
        currentMax = 1
        currentMin = 1

        for num in nums:
            if num == 0:
                currentMax = 1
                currentMin = 1
            else:
                tmp = num * currentMax
                currentMax = max(tmp, num * currentMin, num)
                currentMin = min(tmp, num * currentMin, num)
            
                result = max(result, currentMax)

        return result

