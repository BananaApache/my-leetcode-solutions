class Solution:
    # def binarySearch(self, nums)
    def findMin(self, nums: List[int]) -> int:
        
        result = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            middle = (left + right) // 2

            if nums[middle] >= nums[left]:
                # search right
                result = min(result, nums[middle])
                left = middle + 1
            else:
                # search left
                result = min(result, nums[middle])
                right = middle - 1

        return result
        
