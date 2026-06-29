class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # GREEDY SOLUTION

        #  0 1 2 3 4
        # [2,3,1,1,4]
        
        result = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            maxJump = 0
            for index in range(left, right + 1):
                maxJump = max(maxJump, index + nums[index])
            left = right + 1
            right = maxJump
            result += 1
        
        return result

        # DP SOLUTION
        # goal = len(nums) - 1
        # dp = [len(nums) + 1] * len(nums)
        # dp[-1] = 0
        
        # for index in range(len(nums) - 1, -1, -1):
        #     if (nums[index] + index) >= goal:
        #         for jump in range(index, min(nums[index] + index + 1, len(nums))):
        #             dp[index] = min(dp[index], 1 + dp[jump])
        #         goal = index
        
        # print(dp)
        
        # return dp[0]

