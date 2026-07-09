class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False] * (len(nums))
        dp[-1] = True

        for index in range(len(nums) - 1, -1, -1):
            maxJump = nums[index]
            for jump in range(maxJump, 0, -1):
                if index + jump >= len(dp) or dp[index + jump] is True:
                    dp[index] = True
                    break
        
        return dp[0]

