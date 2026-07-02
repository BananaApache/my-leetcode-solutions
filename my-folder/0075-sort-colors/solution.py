class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        right = len(nums) - 1

        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1

        
        # O(n) space, O(n) time
        # freq = defaultdict(int)
        # for num in nums:
        #     freq[num] += 1
        
        # index = 0
        # for num in range(3):
        #     val = freq[num]
        #     while val:
        #         nums[index] = num
        #         val -= 1
        #         index += 1

