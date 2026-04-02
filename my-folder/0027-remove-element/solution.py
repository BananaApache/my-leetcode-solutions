class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) < 1:
            return 0
        
        maxNum = max(nums)
        count = len(nums)
        for index in range(len(nums)):
            if nums[index] == val:
                count -= 1
                nums[index] = maxNum + 1

        nums.sort()
        
        return count

