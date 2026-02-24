class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # freq = {
        #     0: 0,
        #     1: 0,
        #     2: 0
        # }

        # for num in nums:
        #     freq[num] += 1

        # index = 0
        # for color, count in freq.items():
        #     for _ in range(0, count):
        #         nums[index] = color
        #         index += 1

        # NO EXTRA SPACE

        # three pointers?

        # middle always moving
        # stop when middle reaches right
        # left moves when it sees a zero
        # right moves when it sees a two
        # if middle sees a two, it swaps it with right
        # if middle sees a zero, it swaps with left
        # when swap occurs, check all pointers again?

        def swap(pos1, pos2):
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1]

        left = 0
        middle = 0
        right = len(nums) - 1
                
        while middle <= right:
            if nums[middle] == 2:
                swap(middle, right)
                right -= 1
                middle -= 1
            elif nums[middle] == 0:
                swap(middle, left)
                left += 1

            middle += 1

