class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # my brute force
        # jump = 1
        # while jump < len(nums):
        #     for index in range(len(nums)):
        #         if index + jump < len(nums) and nums[index] == nums[index + jump]:
        #             return nums[index]
        #     jump += 1

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast: # stop when they same
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        entry = 0
        while entry != slow:
            entry = nums[entry]
            slow = nums[slow]

        return slow
