class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # [1,0,3,12]
        #             
        
        # nums.append("STOP")
        # index = 0
        # current = nums[0]
        # zeroes = 0
        # while current != "STOP":
        #     if current == 0:
        #         nums.pop(index)
        #         nums.append(0)
        #         index -= 1
        #         zeroes += 1
            
        #     index += 1
        #     current = nums[index]

        # nums.pop(len(nums) - zeroes - 1)

        # return nums






        # left = None
        # for right in range(len(nums)):
        #     if nums[right] == 0 and left is None:
        #         left = right
        #     elif nums[right] != 0 and left is not None:
        #         # swap
        #         nums[left] = nums[right]
        #         nums[right] = 0
        #         left += 1

        # return nums


        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums

