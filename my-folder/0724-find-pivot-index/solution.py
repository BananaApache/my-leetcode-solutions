class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # # [1,7,3,6,5,6]

        # postsum = [0]

        # for num in nums[::-1]:
        #     postsum.append(num + postsum[-1])

        # postsum = postsum[::-1]

        # # postsum = [28, 27, 20, 17, 11, 6, 0]

        # presum = 0

        # for index in range(len(nums) - 1):
        #     if presum == postsum[index + 1]:
        #         return index

        #     presum += nums[index]

        # if presum == 0:
        #     return len(nums) - 1

        # return -1

        presum = 0
        postsum = sum(nums)

        for index in range(len(nums)):
            postsum = postsum - nums[index]

            if presum == postsum:
                return index

            presum = presum + nums[index]

        return -1

