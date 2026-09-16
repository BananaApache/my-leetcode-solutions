class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # cases:
        # LEFT > RIGHT
        #   MID > RIGHT -> look right
        #   MID < RIGHT -> look left
        # LEFT < RIGHT -> return num at LEFT

        left = 0
        right = len(nums) - 1
        result = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[left] > nums[right]:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                result = min(result, nums[mid])
            else:
                result = min(result, nums[left])
                break
        return result

