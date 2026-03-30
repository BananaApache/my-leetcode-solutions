class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            # case middle in LEFT portion
            if nums[left] > nums[right] and nums[left] <= nums[middle]:
                
                if target > nums[middle] or (target < nums[middle] and target < nums[left]):
                    left = middle + 1
                elif target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    return middle

            # case middle in RIGHT portion
            elif nums[left] > nums[right] and nums[left] > nums[middle]:
                
                if target < nums[middle] or (target > nums[middle] and target > nums[right]):
                    right = middle - 1
                elif target > nums[middle] and target <= nums[right]:
                    left = middle + 1
                else:
                    return middle
            
            else:
                if target > nums[middle]:
                    left = middle + 1
                elif target < nums[middle]:
                    right = middle - 1
                else:
                    return middle

        return -1

