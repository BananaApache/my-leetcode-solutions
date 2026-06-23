class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        result = []
        for index in range(len(nums)):
            if index > 0 and nums[index - 1] == nums[index]:
                continue

            left = index + 1
            right = len(nums) - 1
            target = 0 - nums[index]
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append( (nums[index], nums[left], nums[right]) )
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result

