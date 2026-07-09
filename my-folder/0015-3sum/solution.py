class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        result = []

        prev = None
        for index in range(len(nums) - 2):
            if nums[index] == prev:
                continue

            target = 0 - nums[index]
            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append( [nums[index], nums[left], nums[right]] )
                    curr = nums[right]
                    while right > 0 and nums[right] == curr:
                        right -= 1 
            
            prev = nums[index]
            
        return result

