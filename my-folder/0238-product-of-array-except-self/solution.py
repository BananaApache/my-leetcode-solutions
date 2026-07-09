class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [] # will be post
        count = 1
        for index in range(len(nums)):
            result.append(count * nums[index])
            count = result[index]
        
        # nums [1,2,3,4 ]
        # post [1,2,6,24]

        count = 1
        for index in range(len(result) - 1, 0, -1):
            result[index] = result[index - 1] * count
            count = count * nums[index]
        
        result[0] = count

        return result

        # post = [1] * (len(nums) + 1)
        # pre = [1] * (len(nums) + 1)

        # count = 1
        # for index in range(len(nums)):
        #     post[index + 1] = count * nums[index]
        #     count = post[index + 1]

        # count = 1
        # for index in range(len(nums) - 1, -1, -1):
        #     pre[index] = count * nums[index]
        #     count = pre[index]

        # result = []
        # for index in range(1, len(nums) + 1):
        #     result.append(post[index - 1] * pre[index])
        
        # return result

