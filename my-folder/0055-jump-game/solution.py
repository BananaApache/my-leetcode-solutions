class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # GREEDY APPROACH
        goal = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            jump = nums[index]
            if index + jump >= goal:
                goal = index
        
        return goal == 0

        # DP APPROACH
        # dp = [False] * len(nums)
        # dp[-1] = True

        # for index in range(len(nums) - 1, -1, -1):
        #     if nums[index] != 0:
        #         for jump in range(index, index + nums[index] + 1):
        #             if jump < len(nums) and dp[jump]:
        #                 dp[index] = True
        #                 break
        
        # print(dp)
        
        # return dp[0]

