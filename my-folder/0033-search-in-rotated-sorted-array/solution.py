class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # which half is sorted

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # left half sorted
                if nums[left] <= target and nums[mid] > target:
                    # search left
                    right = mid - 1
                else:
                    # search right
                    left = mid + 1
            elif nums[mid] <= nums[right]: # right half sorted
                if nums[mid] <= target and nums[right] >= target:
                    # search right
                    left = mid + 1
                else:
                    # search left
                    right = mid - 1
        return -1
