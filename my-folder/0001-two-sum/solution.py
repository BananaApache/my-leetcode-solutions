class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        differenceToIndex = {}

        for index in range(len(nums)):
            difference = target - nums[index]

            if nums[index] not in differenceToIndex:
                differenceToIndex[difference] = index
            else:
                return (differenceToIndex[nums[index]], index)

