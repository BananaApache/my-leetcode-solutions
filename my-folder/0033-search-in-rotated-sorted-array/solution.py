class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if target == nums[middle]:
                return middle

            if nums[left] <= nums[middle]:
                # we are in left portion
                if nums[middle] < target or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                # we are in right portion
                if target < nums[middle] or nums[right] < target:
                    right = middle - 1
                else:
                    left = middle + 1
            
        return -1


