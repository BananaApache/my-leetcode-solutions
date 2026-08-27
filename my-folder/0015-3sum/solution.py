class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        result = []

        #   0 1 2 3  4  5    len 6
        # [-1,0,1,2,-1,-4]
        #                 

        nums.sort()
        prev = None
        for index in range(len(nums) - 2):
            if nums[index] == prev:
                continue
            left = index + 1
            right = len(nums) - 1
            target = 0 - nums[index]
            while left < right:
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    result.append([ nums[index],nums[left],nums[right] ])
                    tmp = nums[left]
                    while left < len(nums) and nums[left] == tmp:
                        left += 1
            prev = nums[index]

        return result

