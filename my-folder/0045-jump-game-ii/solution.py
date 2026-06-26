class Solution:
    def jump(self, nums: List[int]) -> int:
        
        goal = len(nums) - 1
        dp = [len(nums) + 1] * len(nums)
        dp[-1] = 0
        
        for index in range(len(nums) - 1, -1, -1):
            if (nums[index] + index) >= goal:
                for jump in range(index, min(nums[index] + index + 1, len(nums))):
                    dp[index] = min(dp[index], 1 + dp[jump])
                goal = index
        
        print(dp)
        
        return dp[0]

