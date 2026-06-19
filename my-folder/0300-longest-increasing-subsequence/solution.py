class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # DP approach

        dp = [1] * len(nums)
        result = 1

        for startIndex in range(len(nums) - 1, -1, -1):
            for index in range(startIndex + 1, len(nums)):
                if nums[startIndex] < nums[index]:
                    dp[startIndex] = max(dp[startIndex], 1 + dp[index])
                    
            result = max(result, dp[startIndex])

        return result

        # DFS BRUTE FORCE APPROACH
        # result = 1
        # hashmap = {}
        
        # def dfs(startIndex, length):
        #     nonlocal result
        #     # base case
        #     if startIndex == len(nums):
        #         result = max(length, result)
        #         hashmap[startIndex] = length
        #         return

        #     for index in range(startIndex, len(nums)):
        #         if nums[startIndex] < nums[index]:
        #             if index in hashmap:
        #                 result = max(result, hashmap[index])
        #             else:
        #                 dfs(index, length + 1)
            
        #     result = max(result, length)

        # for index in range(len(nums)):
        #     dfs(index, 1)

        # return result


