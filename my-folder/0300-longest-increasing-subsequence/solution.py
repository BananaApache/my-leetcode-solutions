class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        curr = [nums[0]]

        # find correct spot to insert num with binary search
        for index in range(1, len(nums)):
            # base cases
            num = nums[index]
            if num > curr[-1]: # num is biggest
                curr.append(num)
            else: # num is in between
                left = 0
                right = len(curr) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if curr[mid] < nums[index]:
                        left = mid + 1
                    else:
                        right = mid - 1
                curr[left] = num
        return len(curr)

        # dp = [1 for _ in range(len(nums))]

        # for index in range(len(dp) - 1, -1, -1):
        #     for jndex in range(index + 1, len(dp)):
        #         if nums[index] < nums[jndex]:
        #             dp[index] = max(1 + dp[jndex], dp[index])
        # print(dp)
        # return max(dp)

